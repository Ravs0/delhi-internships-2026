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
    <title>Delhi Legal Internships - Smart Dashboard</title>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        :root {{
            --bg-base: #f8f9fa; /* Cloud White Matte */
            --bg-surface: #ffffff; /* Pure White for cards */
            --bg-surface-hover: #f1f5f9;
            --accent-main: #1abc9c; /* Matte Turquoise Green */
            --accent-main-hover: #16a085;
            --accent-glow: rgba(26, 188, 156, 0.2);
            --accent-light: #e8f8f5;
            
            --text-primary: #2d3748; /* Matte Charcoal */
            --text-secondary: #718096; /* Matte Gray */
            --border-color: #e2e8f0;
            
            --success: #10b981;
            --danger: #e74c3c;
            --danger-bg: #fdedec;
            
            --font-main: 'Plus Jakarta Sans', sans-serif;
            
            --shadow-matte: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
            --shadow-matte-hover: 0 10px 15px -3px rgba(0, 0, 0, 0.08), 0 4px 6px -2px rgba(0, 0, 0, 0.04);
        }}

        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: var(--font-main);
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
            background: rgba(248, 249, 250, 0.9);
            backdrop-filter: blur(12px);
            border-bottom: 1px solid var(--border-color);
            padding: 1rem 2rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}

        .brand h1 {{
            font-size: 1.5rem;
            color: var(--text-primary);
            font-weight: 700;
            letter-spacing: -0.5px;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }}

        .brand h1 span {{
            color: var(--accent-main);
        }}

        .header-actions {{
            display: flex;
            gap: 1rem;
            align-items: center;
        }}

        .search-container {{
            position: relative;
            width: 350px;
        }}

        .search-container input {{
            width: 100%;
            background: var(--bg-surface);
            border: 1px solid var(--border-color);
            color: var(--text-primary);
            padding: 0.65rem 1rem 0.65rem 2.5rem;
            border-radius: 99px;
            font-size: 0.95rem;
            transition: all 0.2s;
            outline: none;
            box-shadow: inset 0 1px 2px rgba(0,0,0,0.02);
        }}

        .search-container input:focus {{
            border-color: var(--accent-main);
            box-shadow: 0 0 0 3px var(--accent-glow);
        }}

        .search-container input::placeholder {{
            color: #a0aec0;
        }}

        .search-icon {{
            position: absolute;
            left: 1rem;
            top: 50%;
            transform: translateY(-50%);
            color: var(--text-secondary);
            font-size: 1.1rem;
        }}

        .analyzer-btn {{
            background: var(--accent-main);
            color: white;
            border: none;
            padding: 0.65rem 1.25rem;
            border-radius: 99px;
            font-weight: 600;
            font-size: 0.9rem;
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 0.5rem;
            transition: all 0.2s;
            box-shadow: 0 4px 10px var(--accent-glow);
        }}

        .analyzer-btn:hover {{
            transform: translateY(-2px);
            background: var(--accent-main-hover);
            box-shadow: 0 6px 14px rgba(26, 188, 156, 0.3);
        }}

        /* Main Layout */
        .layout {{
            display: flex;
            flex: 1;
            max-width: 1600px;
            margin: 0 auto;
            width: 100%;
            padding: 2rem;
            gap: 2.5rem;
        }}

        /* Sidebar Filters */
        .sidebar {{
            width: 260px;
            flex-shrink: 0;
        }}

        .sidebar h2 {{
            font-size: 0.75rem;
            text-transform: uppercase;
            letter-spacing: 1px;
            color: var(--text-secondary);
            margin-bottom: 0.75rem;
            font-weight: 700;
            margin-top: 1.5rem;
        }}
        
        .sidebar h2:first-child {{
            margin-top: 0;
        }}

        .filter-group {{
            display: flex;
            flex-direction: column;
            gap: 0.4rem;
        }}

        .filter-btn {{
            background: transparent;
            border: 1px solid transparent;
            color: var(--text-secondary);
            padding: 0.6rem 0.85rem;
            border-radius: 8px;
            cursor: pointer;
            text-align: left;
            transition: all 0.2s;
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 0.95rem;
            font-weight: 500;
        }}

        .filter-btn:hover {{
            background: var(--bg-surface);
            color: var(--text-primary);
        }}

        .filter-btn.active {{
            background: var(--bg-surface);
            color: var(--accent-main);
            border-color: var(--border-color);
            font-weight: 600;
            box-shadow: 0 1px 2px rgba(0,0,0,0.02);
        }}

        .count-badge {{
            background: var(--bg-base);
            color: var(--text-secondary);
            padding: 0.15rem 0.5rem;
            border-radius: 99px;
            font-size: 0.75rem;
            border: 1px solid var(--border-color);
        }}

        .filter-btn.active .count-badge {{
            background: var(--accent-light);
            color: var(--accent-main);
            border-color: var(--accent-light);
        }}
        
        /* Secondary Filters (Pills) */
        .pill-group {{
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
            margin-bottom: 1.5rem;
        }}
        
        .pill {{
            background: var(--bg-surface);
            border: 1px solid var(--border-color);
            color: var(--text-secondary);
            padding: 0.4rem 0.8rem;
            border-radius: 99px;
            font-size: 0.8rem;
            cursor: pointer;
            transition: all 0.2s;
            font-weight: 500;
        }}
        
        .pill:hover {{
            border-color: var(--text-secondary);
            color: var(--text-primary);
        }}
        
        .pill.active {{
            background: var(--accent-main);
            color: white;
            border-color: var(--accent-main);
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
            font-size: 1.35rem;
            font-weight: 700;
            color: var(--text-primary);
        }}

        .results-count {{
            color: var(--text-secondary);
            font-size: 0.9rem;
            background: var(--bg-surface);
            padding: 0.3rem 0.8rem;
            border-radius: 99px;
            border: 1px solid var(--border-color);
            font-weight: 500;
        }}

        /* Grid & Cards */
        .grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 1.25rem;
        }}

        .card {{
            background: var(--bg-surface);
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 1.5rem;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            display: flex;
            flex-direction: column;
            position: relative;
            overflow: hidden;
            box-shadow: var(--shadow-matte);
        }}
        
        /* Matte accent top border effect */
        .card::before {{
            content: '';
            position: absolute;
            top: 0; left: 0; right: 0;
            height: 3px;
            background: var(--accent-main);
            opacity: 0;
            transition: opacity 0.3s;
        }}

        .card:hover {{
            transform: translateY(-4px);
            border-color: rgba(26, 188, 156, 0.3);
            box-shadow: var(--shadow-matte-hover);
        }}
        
        .card:hover::before {{
            opacity: 1;
        }}

        .tags-row {{
            display: flex;
            justify-content: space-between;
            margin-bottom: 1rem;
            align-items: center;
        }}

        .tag-category {{
            font-size: 0.7rem;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            color: var(--accent-main);
            font-weight: 700;
            background: var(--accent-light);
            padding: 0.3rem 0.6rem;
            border-radius: 6px;
        }}

        .tag-urgent {{
            background: var(--danger-bg);
            color: var(--danger);
            padding: 0.3rem 0.6rem;
            border-radius: 6px;
            font-size: 0.7rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}

        .card h3 {{
            font-size: 1.15rem;
            margin-bottom: 0.4rem;
            color: var(--text-primary);
            line-height: 1.4;
            font-weight: 700;
        }}

        .focus-area {{
            color: var(--text-secondary);
            font-size: 0.85rem;
            margin-bottom: 1.25rem;
            font-weight: 500;
        }}

        .meta-list {{
            margin-bottom: 1.5rem;
        }}

        .meta-item {{
            display: flex;
            align-items: flex-start;
            font-size: 0.85rem;
            margin-bottom: 0.6rem;
        }}

        .meta-label {{
            color: var(--text-secondary);
            min-width: 75px;
            font-weight: 600;
        }}

        .meta-value {{
            color: var(--text-primary);
            font-weight: 500;
        }}

        .meta-value.paid {{
            color: var(--accent-main);
            background: var(--accent-light);
            padding: 0.1rem 0.4rem;
            border-radius: 4px;
            font-size: 0.8rem;
        }}
        
        .match-score {{
            display: flex;
            align-items: center;
            gap: 0.5rem;
            background: var(--accent-light);
            color: var(--accent-main);
            padding: 0.5rem;
            border-radius: 6px;
            font-weight: 700;
            font-size: 0.9rem;
            margin-bottom: 1rem;
            border: 1px solid rgba(26, 188, 156, 0.2);
        }}

        .card-footer {{
            margin-top: auto;
            border-top: 1px solid var(--border-color);
            padding-top: 1.25rem;
        }}

        .apply-btn {{
            display: block;
            width: 100%;
            text-align: center;
            background: var(--bg-base);
            border: 1px solid var(--border-color);
            color: var(--text-primary);
            padding: 0.6rem;
            border-radius: 8px;
            text-decoration: none;
            font-size: 0.9rem;
            font-weight: 600;
            transition: all 0.2s;
        }}

        .apply-btn:hover {{
            background: var(--accent-main);
            border-color: var(--accent-main);
            color: white;
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

        /* CV Analyzer Modal */
        .modal-overlay {{
            position: fixed;
            top: 0; left: 0; right: 0; bottom: 0;
            background: rgba(45, 55, 72, 0.5);
            backdrop-filter: blur(4px);
            z-index: 1000;
            display: none;
            justify-content: center;
            align-items: center;
            padding: 2rem;
        }}
        
        .modal-overlay.active {{
            display: flex;
        }}

        .modal-content {{
            background: var(--bg-surface);
            border: 1px solid var(--border-color);
            border-radius: 16px;
            width: 100%;
            max-width: 700px;
            max-height: 90vh;
            overflow-y: auto;
            position: relative;
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
        }}
        
        .modal-header {{
            padding: 1.5rem 2rem;
            border-bottom: 1px solid var(--border-color);
            display: flex;
            justify-content: space-between;
            align-items: center;
            position: sticky;
            top: 0;
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(8px);
            z-index: 10;
        }}
        
        .modal-header h2 {{
            font-size: 1.25rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
            color: var(--text-primary);
        }}
        
        .modal-close {{
            background: transparent;
            border: none;
            color: var(--text-secondary);
            font-size: 1.5rem;
            cursor: pointer;
            transition: color 0.2s;
        }}
        
        .modal-close:hover {{
            color: var(--danger);
        }}
        
        .modal-body {{
            padding: 2rem;
        }}
        
        .cv-textarea {{
            width: 100%;
            height: 200px;
            background: var(--bg-base);
            border: 1px solid var(--border-color);
            color: var(--text-primary);
            padding: 1rem;
            border-radius: 8px;
            resize: vertical;
            font-family: var(--font-main);
            font-size: 0.95rem;
            line-height: 1.5;
            margin-bottom: 1.5rem;
            outline: none;
            transition: border-color 0.2s;
        }}
        
        .cv-textarea:focus {{
            border-color: var(--accent-main);
            box-shadow: 0 0 0 3px var(--accent-glow);
        }}
        
        .analyze-action-btn {{
            width: 100%;
            padding: 1rem;
            background: var(--accent-main);
            color: white;
            border: none;
            border-radius: 8px;
            font-size: 1rem;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.2s;
            box-shadow: 0 4px 6px rgba(26, 188, 156, 0.2);
        }}

        .analyze-action-btn:hover:not(:disabled) {{
            background: var(--accent-main-hover);
            transform: translateY(-1px);
        }}
        
        .analyze-action-btn:disabled {{
            opacity: 0.7;
            cursor: not-allowed;
            transform: none;
        }}
        
        .loader {{
            display: none;
            text-align: center;
            margin: 2rem 0;
            color: var(--accent-main);
            font-weight: 600;
        }}
        
        #match-results-container {{
            margin-top: 2rem;
            display: none;
        }}
        
        #match-results-container h3 {{
            margin-bottom: 1rem;
            color: var(--text-primary);
            padding-top: 1.5rem;
            border-top: 1px solid var(--border-color);
            font-weight: 700;
        }}
        
        .results-grid {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 1rem;
        }}
        
        @media (max-width: 900px) {{
            .layout {{ flex-direction: column; padding: 1rem; }}
            .sidebar {{ width: 100%; }}
            .search-container {{ width: 100%; margin-top: 1rem; }}
            header {{ flex-direction: column; align-items: flex-start; }}
            .header-actions {{ width: 100%; flex-direction: column; align-items: stretch; margin-top: 1rem; gap: 0.5rem; }}
            .filter-group {{ flex-direction: row; overflow-x: auto; padding-bottom: 0.5rem; scrollbar-width: none; }}
            .filter-btn {{ white-space: nowrap; }}
            .results-grid {{ grid-template-columns: 1fr; }}
        }}
    </style>
</head>
<body>

    <header>
        <div class="brand">
            <h1>LocalHire<span>.</span></h1>
        </div>
        <div class="header-actions">
            <div class="search-container">
                <span class="search-icon">🔍</span>
                <input type="text" id="search" placeholder="Search by firm, focus, or keyword...">
            </div>
            <button class="analyzer-btn" onclick="openModal()">
                <svg width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
                CV Matcher
            </button>
        </div>
    </header>

    <div class="layout">
        <aside class="sidebar">
            <h2>Primary Category</h2>
            <div class="filter-group" id="filters">
                <button class="filter-btn active" data-filter="all">
                    <span>All Opportunities</span> <span class="count-badge" id="count-all">0</span>
                </button>
                <button class="filter-btn" data-filter="firm">
                    <span>Law Firms</span> <span class="count-badge" id="count-firm">0</span>
                </button>
                <button class="filter-btn" data-filter="litigation">
                    <span>Chambers & Litigation</span> <span class="count-badge" id="count-litigation">0</span>
                </button>
                <button class="filter-btn" data-filter="govt">
                    <span>Govt & Statutory</span> <span class="count-badge" id="count-govt">0</span>
                </button>
                <button class="filter-btn" data-filter="policy">
                    <span>Policy & NGOs</span> <span class="count-badge" id="count-policy">0</span>
                </button>
            </div>
            
            <h2>Quick Filters</h2>
            <div class="pill-group">
                <button class="pill" data-quick="urgent">🔥 Urgent</button>
                <button class="pill" data-quick="paid">💰 Paid</button>
                <button class="pill" data-quick="ip">💡 Intellectual Property</button>
                <button class="pill" data-quick="corp">🏢 Corporate / M&A</button>
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

    <!-- CV Analyzer Modal -->
    <div class="modal-overlay" id="cv-modal">
        <div class="modal-content">
            <div class="modal-header">
                <h2>AI-Powered CV Matcher</h2>
                <button class="modal-close" onclick="closeModal()">×</button>
            </div>
            <div class="modal-body">
                <p style="color: var(--text-secondary); font-size: 0.95rem; margin-bottom: 1rem; line-height: 1.5;">
                    Paste the text of your CV below. Our matching algorithm analyzes your experience to suggest the top 6 internships for you from our database. <br><span style="color: var(--accent-main); font-weight: 500;">Data is processed 100% locally in your browser.</span>
                </p>
                <textarea id="cv-input" class="cv-textarea" placeholder="Paste your CV text here (Projects, Experience, Skills, bio)..."></textarea>
                <button class="analyze-action-btn" id="analyze-btn" onclick="analyzeCV()">Analyze & Find Matches</button>
                
                <div class="loader" id="loader">
                    Running Semantic Analysis...
                </div>
                
                <div id="match-results-container">
                    <h3>Top Recommended Matches</h3>
                    <div class="results-grid" id="match-grid"></div>
                </div>
            </div>
        </div>
    </div>

    <script>
        {internships_data}

        // DOM Elements
        const grid = document.getElementById('grid');
        const filterBtns = document.querySelectorAll('.filter-btn');
        const quickPills = document.querySelectorAll('.pill');
        const searchInput = document.getElementById('search');
        const resultsCount = document.getElementById('results-count');
        const currentViewTitle = document.getElementById('current-view-title');

        // State
        let currentFilter = 'all';
        let searchQuery = '';
        let activeQuickFilters = [];

        function getCategoryName(cat) {{
            const names = {{
                'firm': 'Law Firm',
                'litigation': 'Chambers & Litigation',
                'govt': 'Govt & Statutory',
                'policy': 'Policy & NGO'
            }};
            return names[cat] || cat;
        }}
        
        function isPaid(item) {{
            return item.stipend.toLowerCase().includes('paid') || item.stipend.includes('₹');
        }}

        function createCardHTML(item, showScore = false) {{
            const paid = isPaid(item);
            let html = `
                <div class="card">
                    <div class="tags-row">
                        <span class="tag-category">${{getCategoryName(item.category)}}</span>
                        ${{item.urgent ? '<span class="tag-urgent">Urgent</span>' : ''}}
                    </div>
                    
                    <h3>${{item.title}}</h3>
                    <div class="focus-area">${{item.focus}}</div>
            `;
            
            if (showScore) {{
                html += `
                    <div class="match-score">
                        <svg width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>
                        ${{item.matchScore}}% Match Score
                    </div>
                `;
            }}
            
            html += `
                    <div class="meta-list">
                        <div class="meta-item">
                            <span class="meta-label">Deadline:</span>
                            <span class="meta-value">${{item.deadline}}</span>
                        </div>
                        <div class="meta-item">
                            <span class="meta-label">Stipend:</span>
                            <span class="meta-value ${{paid ? 'paid' : ''}}">${{item.stipend}}</span>
                        </div>
                    </div>

                    <div class="card-footer">
                        <a href="${{item.apply}}" target="_blank" class="apply-btn">Apply / Details</a>
                    </div>
                </div>
            `;
            return html;
        }}

        function render(data) {{
            let finalHtml = '';
            resultsCount.textContent = `${{data.length}} results`;

            if(data.length === 0) {{
                grid.innerHTML = '<div class="empty-state"><h3>No internships found.</h3><p>Try adjusting your search criteria.</p></div>';
                return;
            }}

            data.forEach(item => {{
                finalHtml += createCardHTML(item);
            }});
            
            grid.innerHTML = finalHtml;
        }}

        function updateCounts() {{
            document.getElementById('count-all').textContent = internships.length;
            document.getElementById('count-firm').textContent = internships.filter(i => i.category === 'firm').length;
            document.getElementById('count-litigation').textContent = internships.filter(i => i.category === 'litigation').length;
            document.getElementById('count-govt').textContent = internships.filter(i => i.category === 'govt').length;
            document.getElementById('count-policy').textContent = internships.filter(i => i.category === 'policy').length;
        }}

        function filterData() {{
            let filtered = internships;
            
            // Category Filter
            if(currentFilter !== 'all') {{
                filtered = filtered.filter(i => i.category === currentFilter);
                const btnSpan = document.querySelector(`.filter-btn[data-filter="${{currentFilter}}"] span:first-child`).textContent;
                currentViewTitle.textContent = btnSpan;
            }} else {{
                currentViewTitle.textContent = "All Opportunities";
            }}

            // Quick Filters
            if (activeQuickFilters.includes('urgent')) {{
                filtered = filtered.filter(i => i.urgent);
            }}
            if (activeQuickFilters.includes('paid')) {{
                filtered = filtered.filter(i => isPaid(i));
            }}
            if (activeQuickFilters.includes('ip')) {{
                filtered = filtered.filter(i => i.focus.toLowerCase().includes('ip') || i.focus.toLowerCase().includes('intellectual property'));
            }}
            if (activeQuickFilters.includes('corp')) {{
                filtered = filtered.filter(i => i.focus.toLowerCase().includes('corporate') || i.focus.toLowerCase().includes('m&a') || i.focus.toLowerCase().includes('commercial'));
            }}

            // Search Filter
            if(searchQuery) {{
                const q = searchQuery.toLowerCase();
                filtered = filtered.filter(i => 
                    i.title.toLowerCase().includes(q) || 
                    i.focus.toLowerCase().includes(q)
                );
            }}
            
            // Update Title if quick filters applied
            if (activeQuickFilters.length > 0 && currentFilter === 'all') {{
                currentViewTitle.textContent = "Filtered Results";
            }}
            
            render(filtered);
        }}

        // Event Listeners
        filterBtns.forEach(btn => {{
            btn.addEventListener('click', (e) => {{
                const targetBtn = e.target.closest('.filter-btn');
                filterBtns.forEach(b => b.classList.remove('active'));
                targetBtn.classList.add('active');
                currentFilter = targetBtn.getAttribute('data-filter');
                filterData();
            }});
        }});
        
        quickPills.forEach(pill => {{
            pill.addEventListener('click', (e) => {{
                const q = e.target.getAttribute('data-quick');
                if (activeQuickFilters.includes(q)) {{
                    activeQuickFilters = activeQuickFilters.filter(f => f !== q);
                    e.target.classList.remove('active');
                }} else {{
                    activeQuickFilters.push(q);
                    e.target.classList.add('active');
                }}
                filterData();
            }});
        }});

        searchInput.addEventListener('input', (e) => {{
            searchQuery = e.target.value;
            filterData();
        }});
        
        /* Modal & Analyzer Logic */
        const modal = document.getElementById('cv-modal');
        function openModal() {{ modal.classList.add('active'); document.body.style.overflow = 'hidden'; }}
        function closeModal() {{ modal.classList.remove('active'); document.body.style.overflow = 'auto'; }}
        
        // Close modal on outside click
        modal.addEventListener('click', (e) => {{
            if(e.target === modal) closeModal();
        }});
        
        function analyzeCV() {{
            const text = document.getElementById('cv-input').value.toLowerCase();
            if(!text.trim()) {{
                alert("Please paste your CV text first.");
                return;
            }}
            
            const btn = document.getElementById('analyze-btn');
            const loader = document.getElementById('loader');
            const resultsCtr = document.getElementById('match-results-container');
            const matchGrid = document.getElementById('match-grid');
            
            btn.disabled = true;
            btn.textContent = "Analyzing...";
            loader.style.display = "block";
            resultsCtr.style.display = "none";
            
            // Artificial delay to simulate heavy processing
            setTimeout(() => {{
                // Matching Algorithm
                let scored = internships.map(item => {{
                    let score = 30; // Base score
                    const focus = item.focus.toLowerCase();
                    const title = item.title.toLowerCase();
                    const cat = item.category;
                    
                    // Experience modifier Length heuristic
                    const isExperienced = text.length > 1500;
                    
                    // Domain specific scoring
                    if (focus.includes('ip') || focus.includes('intellectual property') || focus.includes('patent') || focus.includes('trademark')) {{
                        if (text.includes('ip ') || text.includes('intellectual property') || text.includes('patent') || text.includes('trademark')) score += 35;
                        if (text.includes('technology law')) score += 15;
                    }}
                    
                    if (focus.includes('corporate') || focus.includes('m&a') || focus.includes('commercial')) {{
                        if (text.includes('corporate') || text.includes('merger') || text.includes('acquisition') || text.includes('transactional') || text.includes('commercial') || text.includes('due diligence')) score += 35;
                        if (text.includes('contract drafting')) score += 15;
                    }}
                    
                    if (cat === 'litigation' || focus.includes('dispute') || focus.includes('arbitration') || focus.includes('court')) {{
                        if (text.includes('litigation') || text.includes('dispute') || text.includes('arbitration') || text.includes('moot court') || text.includes('drafting') || text.includes('research')) score += 30;
                        if (text.includes('high court') || text.includes('supreme court')) score += 15;
                    }}
                    
                    if (cat === 'policy' || cat === 'govt' || focus.includes('policy') || focus.includes('human rights') || focus.includes('research')) {{
                        if (text.includes('policy') || text.includes('human rights') || (text.match(/research/g) || []).length > 2 || text.includes('ngo') || text.includes('publication') || text.includes('paper')) score += 35;
                    }}
                    
                    // Exact keyword matches (firm name)
                    const keywords = title.split(' ').filter(w => w.length > 3);
                    keywords.forEach(kw => {{
                        if(text.includes(kw)) score += 15;
                    }});
                    
                    // Paid preference bump if CV suggests high value/experience
                    if(isExperienced && isPaid(item)) score += 10;
                    
                    // Randomizer to prevent identical scores
                    score += (title.charCodeAt(0) % 8);
                    
                    // Caps
                    if (score > 98) score = 98;
                    
                    return {{ ...item, matchScore: score }};
                }});
                
                // Sort by highest score
                scored.sort((a, b) => b.matchScore - a.matchScore);
                
                // Render top 6 matches
                const topMatches = scored.slice(0, 6);
                let resultsHtml = '';
                topMatches.forEach(match => {{
                    resultsHtml += createCardHTML(match, true);
                }});
                
                matchGrid.innerHTML = resultsHtml;
                
                // Reset UI
                loader.style.display = "none";
                resultsCtr.style.display = "block";
                btn.disabled = false;
                btn.textContent = "Re-Analyze CV";
                
            }}, 1500);
        }}

        // Init
        updateCounts();
        filterData();
    </script>
</body>
</html>
"""

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Vercel-ready Matte White & Turquoise UI injected successfully!")
