import re

html_path = 'index.html'

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'(const internships = \[\s*.*?\s*\];)', content, re.DOTALL)
if not match:
    print("Could not find internships array.")
    exit(1)

internships_data = match.group(1)

new_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Delhi Legal Internships 2026</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        :root {{
            --bg-base: #0a0f1c;
            --bg-surface: #141b2d;
            --bg-surface-hover: #1e293b;
            --accent-gold: #d4af37;
            --accent-gold-hover: #f1c40f;
            --text-primary: #f8fafc;
            --text-secondary: #94a3b8;
            --border-color: #1e293b;
            --success: #10b981;
            --danger: #ef4444;
            --danger-bg: rgba(239, 68, 68, 0.1);
        }}

        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Inter', sans-serif;
        }}

        body {{
            background-color: var(--bg-base);
            color: var(--text-primary);
            display: flex;
            flex-direction: column;
            min-height: 100vh;
        }}

        /* Header / Nav */
        header {{
            position: sticky;
            top: 0;
            z-index: 100;
            background: rgba(10, 15, 28, 0.85);
            backdrop-filter: blur(12px);
            border-bottom: 1px solid var(--border-color);
            padding: 1.25rem 2rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}

        .brand h1 {{
            font-size: 1.5rem;
            color: var(--text-primary);
            font-weight: 600;
            letter-spacing: -0.5px;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }}

        .brand h1 span {{
            color: var(--accent-gold);
        }}

        .search-container {{
            position: relative;
            width: 400px;
        }}

        .search-container input {{
            width: 100%;
            background: var(--bg-surface);
            border: 1px solid var(--border-color);
            color: var(--text-primary);
            padding: 0.75rem 1rem 0.75rem 2.5rem;
            border-radius: 8px;
            font-size: 0.95rem;
            transition: all 0.2s;
            outline: none;
        }}

        .search-container input:focus {{
            border-color: var(--accent-gold);
            box-shadow: 0 0 0 2px rgba(212, 175, 55, 0.2);
        }}

        .search-icon {{
            position: absolute;
            left: 1rem;
            top: 50%;
            transform: translateY(-50%);
            color: var(--text-secondary);
            font-size: 1.2rem;
        }}

        /* Main Layout */
        .layout {{
            display: flex;
            flex: 1;
            max-width: 1600px;
            margin: 0 auto;
            width: 100%;
            padding: 2rem;
            gap: 2rem;
        }}

        /* Sidebar Filters */
        .sidebar {{
            width: 280px;
            flex-shrink: 0;
        }}

        .sidebar h2 {{
            font-size: 0.85rem;
            text-transform: uppercase;
            letter-spacing: 1px;
            color: var(--text-secondary);
            margin-bottom: 1rem;
            font-weight: 600;
        }}

        .filter-group {{
            display: flex;
            flex-direction: column;
            gap: 0.5rem;
        }}

        .filter-btn {{
            background: transparent;
            border: 1px solid transparent;
            color: var(--text-secondary);
            padding: 0.75rem 1rem;
            border-radius: 8px;
            cursor: pointer;
            text-align: left;
            transition: all 0.2s;
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 0.95rem;
        }}

        .filter-btn:hover {{
            background: var(--bg-surface);
            color: var(--text-primary);
        }}

        .filter-btn.active {{
            background: var(--bg-surface);
            color: var(--accent-gold);
            border-color: var(--border-color);
            font-weight: 500;
        }}

        .count-badge {{
            background: var(--bg-surface-hover);
            color: var(--text-secondary);
            padding: 0.15rem 0.5rem;
            border-radius: 99px;
            font-size: 0.75rem;
        }}

        .filter-btn.active .count-badge {{
            background: rgba(212, 175, 55, 0.15);
            color: var(--accent-gold);
        }}

        /* Content Area */
        .content {{
            flex: 1;
        }}

        .content-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 1.5rem;
        }}

        .content-header h2 {{
            font-size: 1.25rem;
            font-weight: 500;
        }}

        .results-count {{
            color: var(--text-secondary);
            font-size: 0.9rem;
        }}

        /* Grid & Cards */
        .grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
            gap: 1.25rem;
        }}

        .card {{
            background: var(--bg-surface);
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 1.5rem;
            transition: all 0.2s;
            display: flex;
            flex-direction: column;
        }}

        .card:hover {{
            transform: translateY(-2px);
            border-color: rgba(212, 175, 55, 0.4);
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.2);
        }}

        .tags-row {{
            display: flex;
            justify-content: space-between;
            margin-bottom: 1rem;
            align-items: center;
        }}

        .tag-category {{
            font-size: 0.75rem;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            color: var(--text-secondary);
            font-weight: 600;
            background: var(--bg-base);
            padding: 0.3rem 0.6rem;
            border-radius: 4px;
            border: 1px solid var(--border-color);
        }}

        .tag-urgent {{
            background: var(--danger-bg);
            color: var(--danger);
            padding: 0.3rem 0.6rem;
            border-radius: 4px;
            font-size: 0.7rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            animation: pulse 2s infinite;
        }}

        @keyframes pulse {{
            0% {{ opacity: 1; }}
            50% {{ opacity: 0.7; }}
            100% {{ opacity: 1; }}
        }}

        .card h3 {{
            font-size: 1.15rem;
            margin-bottom: 0.4rem;
            color: var(--text-primary);
            line-height: 1.4;
        }}

        .focus-area {{
            color: var(--accent-gold);
            font-size: 0.85rem;
            margin-bottom: 1.5rem;
            font-weight: 500;
        }}

        .meta-list {{
            margin-bottom: 1.5rem;
        }}

        .meta-item {{
            display: flex;
            align-items: flex-start;
            font-size: 0.9rem;
            margin-bottom: 0.5rem;
        }}

        .meta-label {{
            color: var(--text-secondary);
            min-width: 80px;
        }}

        .meta-value {{
            color: var(--text-primary);
        }}

        .meta-value.paid {{
            color: var(--success);
            font-weight: 600;
        }}

        .card-footer {{
            margin-top: auto;
            border-top: 1px solid var(--border-color);
            padding-top: 1rem;
        }}

        .apply-btn {{
            display: block;
            width: 100%;
            text-align: center;
            background: transparent;
            border: 1px solid var(--accent-gold);
            color: var(--accent-gold);
            padding: 0.6rem;
            border-radius: 6px;
            text-decoration: none;
            font-size: 0.95rem;
            font-weight: 600;
            transition: all 0.2s;
        }}

        .apply-btn:hover {{
            background: var(--accent-gold);
            color: #000;
        }}

        .empty-state {{
            text-align: center;
            padding: 4rem;
            color: var(--text-secondary);
            grid-column: 1 / -1;
            background: var(--bg-surface);
            border-radius: 12px;
            border: 1px dashed var(--border-color);
        }}

        @media (max-width: 900px) {{
            .layout {{ flex-direction: column; padding: 1rem; }}
            .sidebar {{ width: 100%; }}
            .search-container {{ width: 200px; }}
            .filter-group {{ flex-direction: row; overflow-x: auto; padding-bottom: 0.5rem; }}
            .filter-btn {{ white-space: nowrap; }}
        }}
    </style>
</head>
<body>

    <header>
        <div class="brand">
            <h1><span>🏛️</span> Internships '26</h1>
        </div>
        <div class="search-container">
            <span class="search-icon">🔍</span>
            <input type="text" id="search" placeholder="Search by firm, focus, or keyword...">
        </div>
    </header>

    <div class="layout">
        <aside class="sidebar">
            <h2>Categories</h2>
            <div class="filter-group" id="filters">
                <button class="filter-btn active" data-filter="all">
                    <span>All Opportunities</span> <span class="count-badge" id="count-all">0</span>
                </button>
                <button class="filter-btn" data-filter="urgent">
                    <span>🔥 Urgent Deadlines</span> <span class="count-badge" id="count-urgent">0</span>
                </button>
                <button class="filter-btn" data-filter="firm">
                    <span>💼 Law Firms</span> <span class="count-badge" id="count-firm">0</span>
                </button>
                <button class="filter-btn" data-filter="litigation">
                    <span>⚖️ Chambers & Litigation</span> <span class="count-badge" id="count-litigation">0</span>
                </button>
                <button class="filter-btn" data-filter="govt">
                    <span>🏛️ Govt & Statutory</span> <span class="count-badge" id="count-govt">0</span>
                </button>
                <button class="filter-btn" data-filter="policy">
                    <span>🌍 Think Tanks & NGOs</span> <span class="count-badge" id="count-policy">0</span>
                </button>
            </div>
        </aside>

        <main class="content">
            <div class="content-header">
                <h2 id="current-view-title">All Opportunities</h2>
                <span class="results-count" id="results-count">0 results</span>
            </div>
            <div class="grid" id="grid">
                <!-- Cards injected here -->
            </div>
        </main>
    </div>

    <script>
        {internships_data}

        // DOM Elements
        const grid = document.getElementById('grid');
        const filterBtns = document.querySelectorAll('.filter-btn');
        const searchInput = document.getElementById('search');
        const resultsCount = document.getElementById('results-count');
        const currentViewTitle = document.getElementById('current-view-title');

        // State
        let currentFilter = 'all';
        let searchQuery = '';

        function getCategoryName(cat) {{
            const names = {{
                'firm': 'Law Firm',
                'litigation': 'Chambers / Litigation',
                'govt': 'Govt & Statutory',
                'policy': 'Think Tank / NGO'
            }};
            return names[cat] || cat;
        }}

        function render(data) {{
            grid.innerHTML = '';
            resultsCount.textContent = `${{data.length}} results`;

            if(data.length === 0) {{
                grid.innerHTML = '<div class="empty-state"><h3>No internships found.</h3><p>Try adjusting your search criteria.</p></div>';
                return;
            }}

            // Display in reverse order ideally to show newest first, but let's keep array order
            data.forEach(item => {{
                const isPaid = item.stipend.toLowerCase().includes('paid') || item.stipend.includes('₹');
                
                const card = document.createElement('div');
                card.className = 'card';
                card.innerHTML = `
                    <div class="tags-row">
                        <span class="tag-category">${{getCategoryName(item.category)}}</span>
                        ${{item.urgent ? '<span class="tag-urgent">Urgent</span>' : ''}}
                    </div>
                    
                    <h3>${{item.title}}</h3>
                    <div class="focus-area">${{item.focus}}</div>
                    
                    <div class="meta-list">
                        <div class="meta-item">
                            <span class="meta-label">Deadline:</span>
                            <span class="meta-value">${{item.deadline}}</span>
                        </div>
                        <div class="meta-item">
                            <span class="meta-label">Stipend:</span>
                            <span class="meta-value ${{isPaid ? 'paid' : ''}}">${{item.stipend}}</span>
                        </div>
                    </div>

                    <div class="card-footer">
                        <a href="${{item.apply}}" target="_blank" class="apply-btn">Apply / Details</a>
                    </div>
                `;
                grid.appendChild(card);
            }});
        }}

        function updateCounts() {{
            document.getElementById('count-all').textContent = internships.length;
            document.getElementById('count-urgent').textContent = internships.filter(i => i.urgent).length;
            document.getElementById('count-firm').textContent = internships.filter(i => i.category === 'firm').length;
            document.getElementById('count-litigation').textContent = internships.filter(i => i.category === 'litigation').length;
            document.getElementById('count-govt').textContent = internships.filter(i => i.category === 'govt').length;
            document.getElementById('count-policy').textContent = internships.filter(i => i.category === 'policy').length;
        }}

        function filterData() {{
            let filtered = internships;
            
            // Category Filter
            if(currentFilter !== 'all') {{
                if(currentFilter === 'urgent') {{
                    filtered = filtered.filter(i => i.urgent);
                    currentViewTitle.textContent = "🔥 Urgent Deadlines";
                }} else {{
                    filtered = filtered.filter(i => i.category === currentFilter);
                    const btnSpan = document.querySelector(`.filter-btn[data-filter="${{currentFilter}}"] span:first-child`).textContent;
                    currentViewTitle.textContent = btnSpan;
                }}
            }} else {{
                currentViewTitle.textContent = "All Opportunities";
            }}

            // Search Filter
            if(searchQuery) {{
                const q = searchQuery.toLowerCase();
                filtered = filtered.filter(i => 
                    i.title.toLowerCase().includes(q) || 
                    i.focus.toLowerCase().includes(q)
                );
            }}
            
            render(filtered);
        }}

        // Event Listeners
        filterBtns.forEach(btn => {{
            btn.addEventListener('click', (e) => {{
                // Handle click on nested elements
                const targetBtn = e.target.closest('.filter-btn');
                filterBtns.forEach(b => b.classList.remove('active'));
                targetBtn.classList.add('active');
                currentFilter = targetBtn.getAttribute('data-filter');
                filterData();
            }});
        }});

        searchInput.addEventListener('input', (e) => {{
            searchQuery = e.target.value;
            filterData();
        }});

        // Init
        updateCounts();
        filterData();
    </script>
</body>
</html>
"""

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(new_html)

print("UI successfully upgraded!")
