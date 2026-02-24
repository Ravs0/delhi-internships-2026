export default async function handler(req, res) {
    if (req.method !== 'POST') {
        return res.status(405).json({ message: 'Method Not Allowed' });
    }

    const apiKey = process.env.DEEPSEEK_API_KEY;
    if (!apiKey) {
        return res.status(500).json({ message: 'API key not configured. Please add DEEPSEEK_API_KEY to your Vercel Project Environment Variables.' });
    }

    const { cvText, internships } = req.body;

    if (!cvText || !internships || !Array.isArray(internships)) {
        return res.status(400).json({ message: 'Invalid payload: missing cvText or internships list' });
    }

    // Slim down payload to save context tokens and response time
    const slimInternships = internships.map(i => ({
        id: i.id,
        title: i.title,
        category: i.category,
        focus: i.focus,
        stipend: i.stipend
    }));

    const prompt = `You are an expert legal recruiter acting as an AI Matchmaker.
Match this candidate's CV to the optimal legal internship opportunities in Delhi.

CANDIDATE CV:
"""
${cvText.substring(0, 4000)}
"""

AVAILABLE INTERNSHIPS (JSON FORMAT):
${JSON.stringify(slimInternships)}

TASK: Find the TOP 6 most suitable internships from the list based exclusively on the candidate's skills, experience, and interests.

OUTPUT FORMAT:
Return ONLY a valid JSON object. Do not include markdown like \`\`\`json.
The JSON object must have exactly these 2 keys:
1. "matches": an array containing exactly 6 objects. Each object must have:
   - "id": The integer ID of the internship.
   - "matchScore": An integer from 85 to 99 showing percentage match.
   - "reason": A single, punchy phrase (e.g. "Direct experience in Tech/IP disputes.") explaining why this internship fits the CV. Do not exceed 10 words.
2. "feedback": an array of 3 strings. Each string must be a practical, actionable suggestion on how to improve this CV for legal internships (max 15 words each).`;

    try {
        const response = await fetch('https://api.deepseek.com/v1/chat/completions', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${apiKey}`
            },
            body: JSON.stringify({
                model: 'deepseek-chat',
                messages: [{ role: 'user', content: prompt }],
                temperature: 0.1
            })
        });

        if (!response.ok) {
            const errorText = await response.text();
            console.error('DeepSeek Error:', errorText);
            return res.status(502).json({ message: 'Failed to connect to DeepSeek LLM' });
        }

        const data = await response.json();
        let content = data.choices[0].message.content;
        content = content.replace(/```json/g, '').replace(/```/g, '').trim();

        try {
            const parsed = JSON.parse(content);
            return res.status(200).json(parsed);
        } catch (parseError) {
            return res.status(500).json({ message: 'Failed to parse AI response into JSON', raw: content });
        }

    } catch (err) {
        return res.status(500).json({ message: 'Internal Server Error', details: err.message });
    }
}
