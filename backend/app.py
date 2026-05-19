<!DOCTYPE html>
<html lang="ta">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Supply Chain Vulnerability Visualizer</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        /* Define theme colors and typography based on the goal UI image */
        :root {
            --bg-color: #0d1117;
            --card-bg: #161b22;
            --border-color: #30363d;
            --text-primary: #c9d1d9;
            --text-secondary: #8b949e;
            --accent-blue: #58a6ff;
            
            --risk-critical: #da3633;
            --risk-high: #f85149;
            --risk-medium: #d29922;
            --risk-low: #3fb950;
        }

        body {
            background-color: var(--bg-color);
            color: var(--text-primary);
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji";
        }

        .border-default { border-color: var(--border-color); }
        .text-secondary { color: var(--text-secondary); }
        .bg-card { background-color: var(--card-bg); }

        /* Custom scrollbar to match the theme */
        ::-webkit-scrollbar {
            width: 8px;
            height: 8px;
        }
        ::-webkit-scrollbar-track {
            background: var(--bg-color);
        }
        ::-webkit-scrollbar-thumb {
            background: var(--border-color);
            border-radius: 4px;
        }
    </style>
</head>
<body class="flex min-h-screen">

    <nav class="w-64 bg-card border-r border-default p-4 flex flex-col justify-between">
        <div>
            <div class="flex items-center gap-3 mb-10">
                <svg width="24" height="24" viewBox="0 0 16 16" fill="currentColor" class="text-accent-blue">
                    <path d="M12.5 16a3.5 3.5 0 1 1 0-7 3.5 3.5 0 0 1 0 7Zm.5-5.5a.5.5 0 0 0-1 0v1.5a.5.5 0 0 0 1 0v-1.5Zm0 2a.5.5 0 0 0-1 0v.5a.5.5 0 0 0 1 0v-.5ZM8.5 16a3.5 3.5 0 1 1 0-7 3.5 3.5 0 0 1 0 7Zm-2-2.5a.5.5 0 0 0-1 0v1.5a.5.5 0 0 0 1 0v-1.5Zm0 2a.5.5 0 0 0-1 0v.5a.5.5 0 0 0 1 0v-.5Z"/>
                    <path d="M6 1.5A.5.5 0 0 1 6.5 1h3a.5.5 0 0 1 .5.5v3a.5.5 0 0 1-.5.5h-3A.5.5 0 0 1 6 4.5v-3Z"/>
                    <path d="M1 1.5A.5.5 0 0 1 1.5 1h3a.5.5 0 0 1 .5.5v3a.5.5 0 0 1-.5.5h-3A.5.5 0 0 1 1 4.5v-3ZM6.5 7h3A.5.5 0 0 1 10 7.5v3a.5.5 0 0 1-.5.5h-3A.5.5 0 0 1 6 10.5v-3A.5.5 0 0 1 6.5 7ZM1.5 7h3A.5.5 0 0 1 5 7.5v3A.5.5 0 0 1 4.5 11h-3A.5.5 0 0 1 1 10.5v-3A.5.5 0 0 1 1.5 7Z"/>
                </svg>
                <h1 class="text-lg font-semibold text-primary">SCV Visualizer</h1>
            </div>

            <a href="#" class="flex items-center gap-3 p-3 bg-gray-800 rounded-lg text-accent-blue font-medium mb-3">
                <svg width="18" height="18" fill="currentColor" viewBox="0 0 16 16"><path d="M11 2.5a.5.5 0 0 1 .5-.5h3a.5.5 0 0 1 .5.5v11a.5.5 0 0 1-.5.5h-3a.5.5 0 0 1-.5-.5v-11Z"/><path d="M1 2.5a.5.5 0 0 1 .5-.5h3a.5.5 0 0 1 .5.5v11a.5.5 0 0 1-.5.5h-3a.5.5 0 0 1-.5-.5v-11Z"/><path d="M6 2.5a.5.5 0 0 1 .5-.5h3a.5.5 0 0 1 .5.5v11a.5.5 0 0 1-.5.5h-3a.5.5 0 0 1-.5-.5v-11Z"/></svg>
                Dashboard
            </a>
            <a href="#" class="flex items-center gap-3 p-3 rounded-lg text-secondary hover:text-primary mb-3">
                <svg width="18" height="18" fill="currentColor" viewBox="0 0 16 16"><path d="M8 8.5a.5.5 0 1 1 0-1 .5.5 0 0 1 0 1ZM8 10a1 1 0 1 0 0-2 1 1 0 0 0 0 2Z"/><path d="M8 11.5a.5.5 0 1 1 0-1 .5.5 0 0 1 0 1ZM8 13a1 1 0 1 0 0-2 1 1 0 0 0 0 2Z"/><path d="M8 15a.5.5 0 1 1 0-1 .5.5 0 0 1 0 1ZM8.5 15a.5.5 0 0 1-.5.5H2a.5.5 0 0 1-.5-.5V1a.5.5 0 0 1 .5-.5h11a.5.5 0 0 1 .5.5v14a.5.5 0 0 1-.5.5H8.5V15ZM2 0h11a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V2a2 2 0 0 1 2-2Z"/></svg>
                Dependecy Input
            </a>
            </div>

        <div class="text-xs text-secondary border-t border-default pt-4">
            Last Updated:<br/> <span class="font-mono">May 19, 2026 13:03 IST</span>
        </div>
    </nav>

    <main class="flex-1 p-8">
        
        <header class="mb-10 bg-card p-6 rounded-2xl border border-default shadow-lg">
            <div class="mb-6">
                <h2 class="text-xl font-bold text-primary">Analyze dependencies, detect vulnerabilities, and identify risky packages</h2>
                <p class="text-secondary mt-1">Enter your declared tech stack below to begin the supply chain analysis.</p>
            </div>
            
            <div class="grid grid-cols-3 gap-6">
                <div class="col-span-2">
                    <label for="techStackInput" class="block text-sm font-medium text-primary mb-2">Enter Tech Stack</label>
                    <div class="relative">
                        <input type="text" id="techStackInput" 
                               class="w-full bg-color p-4 rounded-lg border border-default text-primary placeholder:text-secondary" 
                               placeholder="e.g., React Firebase jsonwebtoken lodash FastAPI">
                        <button class="absolute right-3 top-3 bg-accent-blue text-gray-950 font-semibold p-2 px-6 rounded-lg hover:brightness-110">
                            Analyze Vulnerabilities
                        </button>
                    </div>
                </div>
                
                <div class="bg-color p-5 rounded-2xl border border-default flex flex-col items-center">
                    <h3 class="text-sm font-semibold text-secondary mb-4">Overall Risk Score</h3>
                    <div class="relative w-28 h-28 flex items-center justify-center">
                        <svg class="absolute inset-0 w-full h-full transform -rotate-90" viewBox="0 0 120 120">
                          <circle cx="60" cy="60" r="54" fill="none" stroke="currentColor" class="text-gray-800" stroke-width="12"></circle>
                          <circle cx="60" cy="60" r="54" fill="none" stroke="currentColor" class="text-risk-high" stroke-width="12" stroke-dasharray="271 339" stroke-linecap="round"></circle> </svg>
                        <div class="text-center">
                            <span class="text-4xl font-extrabold text-primary">8.2</span>
                            <span class="block text-xs font-semibold text-risk-high">HIGH RISK</span>
                        </div>
                    </div>
                    <p class="text-xs text-secondary mt-3">Score: 8.2 / 10</p>
                </div>
            </div>
        </header>

        <div class="grid grid-cols-3 gap-8">
            
            <div class="col-span-2 bg-card p-6 rounded-2xl border border-default min-h-[500px]">
                <div class="flex justify-between items-start mb-6">
                    <div>
                        <h3 class="text-lg font-semibold text-primary">Dependency Graph</h3>
                        <p class="text-sm text-secondary">Visual map of interconnected package dependencies.</p>
                    </div>
                    <button class="text-xs text-accent-blue font-medium p-1.5 px-4 bg-gray-800 rounded-lg border border-default hover:bg-gray-700">View Fullscreen</button>
                </div>
                
                <div class="relative flex-1 bg-color rounded-xl p-4 flex items-center justify-center border border-dashed border-default">
                    
                    <div class="relative w-full h-96">
                        
                        <div class="absolute inset-0 flex items-center justify-center">
                            <div class="w-36 h-36 bg-gray-800 rounded-full border-2 border-primary flex items-center justify-center text-center p-3 text-sm font-semibold">
                                Your<br/>Application
                            </div>
                        </div>

                        <div class="absolute top-10 left-1/4 w-24 h-24 bg-card rounded-full border-2 border-primary flex flex-col items-center justify-center text-center p-2 text-xs">
                             <img src="https://upload.wikimedia.org/wikipedia/commons/a/a7/React-icon.svg" alt="React" class="w-8 h-8 mb-1">
                             React<br/>v18.2.0
                        </div>
                        <div class="absolute bottom-10 left-1/4 w-24 h-24 bg-card rounded-full border-2 border-primary flex flex-col items-center justify-center text-center p-2 text-xs">
                             <img src="https://upload.wikimedia.org/wikipedia/commons/3/37/Firebase_Logo.svg" alt="Firebase" class="w-8 h-8 mb-1">
                             Firebase<br/>Auth
                        </div>
                        
                        <div class="absolute top-20 right-1/4 w-24 h-24 bg-card rounded-full border-2 border-risk-critical flex flex-col items-center justify-center text-center p-2 text-xs text-risk-critical">
                             <div class="text-xl font-bold mb-1">l</div>
                             lodosh<br/>v4.17.11
                        </div>
                         </div>

                    <div class="absolute bottom-4 left-4 p-3 bg-card/80 backdrop-blur-sm rounded-lg border border-default text-xs flex gap-4">
                        <div class="flex items-center gap-1.5"><span class="w-3 h-3 bg-gray-800 rounded-full border border-primary"></span>Your App</div>
                        <div class="flex items-center gap-1.5"><span class="w-3 h-3 bg-card rounded-full border border-primary"></span>Library</div>
                        <div class="flex items-center gap-1.5"><span class="w-3 h-3 bg-card rounded-full border border-risk-critical"></span>Risky</div>
                    </div>
                </div>
            </div>

            <aside class="space-y-8">
                
                <div class="bg-card p-6 rounded-2xl border border-default">
                    <div class="flex justify-between items-start mb-5">
                        <h3 class="text-md font-semibold text-primary">Top Risky Packages</h3>
                        <a href="#" class="text-xs text-accent-blue font-medium hover:underline">View All</a>
                    </div>
                    
                    <div class="space-y-4">
                        <div class="flex items-start gap-4 p-4 bg-color rounded-xl border border-default">
                            <div class="flex-none text-2xl font-black text-secondary">l</div> <div class="flex-1">
                                <div class="flex items-center justify-between">
                                    <h4 class="font-medium text-primary">lodosh <span class="font-mono text-secondary">v4.17.11</span></h4>
                                    <span class="text-[10px] p-1.5 px-2 bg-risk-critical/15 text-risk-critical font-bold rounded-full">CRITICAL</span>
                                </div>
                                <p class="text-sm font-semibold mt-1">Score: <span class="text-risk-critical">9.6</span></p>
                                <p class="text-xs text-secondary mt-1">CVE-2021-23337</p>
                            </div>
                        </div>
                        
                        </div>
                </div>

                <div class="bg-card p-6 rounded-2xl border border-default">
                    <div class="flex justify-between items-start mb-5">
                        <h3 class="text-md font-semibold text-primary">Recommendations</h3>
                        <a href="#" class="text-xs text-accent-blue font-medium hover:underline">View All</a>
                    </div>
                    
                    <div class="space-y-4 text-sm">
                        <div class="flex gap-3">
                            <svg width="20" height="20" fill="currentColor" viewBox="0 0 16 16" class="text-risk-critical mt-0.5"><path d="M7.002 11a1 1 0 1 1 2 0 1 1 0 0 1-2 0zM7.1 4.995a.905.905 0 1 1 1.8 0l-.35 3.507a.552.552 0 0 1-1.1 0L7.1 4.995z"/><path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zM8 1.5a6.5 6.5 0 1 0 0 13 6.5 6.5 0 0 0 0-13z"/></svg>
                            <div>
                                <p class="text-primary font-medium">Update <span class="font-mono">lodosh</span> to latest version <span class="font-mono">(>=4.17.21)</span></p>
                                <p class="text-xs text-secondary mt-1">Fixes 1 critical vulnerability</p>
                            </div>
                        </div>
                         </div>
                </div>
            </aside>
        </div>

        <footer class="mt-10 bg-card p-6 rounded-2xl border border-default">
            <h3 class="text-lg font-semibold text-primary mb-6">Risk Summary</h3>
            <table class="w-full text-sm text-left border-collapse">
                <thead class="text-xs text-secondary border-b border-default uppercase">
                    <tr>
                        <th scope="col" class="pb-4 pr-6">Component</th>
                        <th scope="col" class="pb-4 pr-6">Type</th>
                        <th scope="col" class="pb-4 pr-6">Version</th>
                        <th scope="col" class="pb-4 pr-6">Risk Score</th>
                        <th scope="col" class="pb-4 pr-6">Risk Level</th>
                        <th scope="col" class="pb-4 pr-6">Issue</th>
                        <th scope="col" class="pb-4">Recommendation</th>
                    </tr>
                </thead>
                <tbody class="text-primary space-y-2">
                    <tr class="border-b border-default/50 hover:bg-color/50">
                        <th scope="row" class="py-4 pr-6 font-medium whitespace-nowrap">lodosh</th>
                        <td class="py-4 pr-6">Library</td>
                        <td class="py-4 pr-6 font-mono text-secondary">4.17.11</td>
                        <td class="py-4 pr-6 text-risk-critical font-semibold">9.6</td>
                        <td class="py-4 pr-6"><span class="text-[10px] p-1.5 px-2 bg-risk-critical/15 text-risk-critical font-bold rounded-full uppercase">Critical</span></td>
                        <td class="py-4 pr-6 font-mono text-secondary">CVE-2021-23337</td>
                        <td class="py-4">Update to >=4.17.21</td>
                    </tr>
                    </tbody>
            </table>
        </footer>
    </main>
<script>
        document.querySelector('button').addEventListener('click', async () => {
            const inputText = document.getElementById('techStackInput').value;
            if (!inputText) return alert("Please enter some packages!");

            try {
                // CHANGE THIS URL STRING BELOW TO YOUR LOCALTUNNEL LINK
                const tunnelUrl = 'http://127.0.0.1:5000'; 
                
                const response = await fetch(`${tunnelUrl}/api/analyze`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ tech_stack: inputText })
                });
                
                const data = await response.json();
                
                // 1. Update Overall Risk Score Panel
                document.querySelector('.text-4xl').innerText = data.overall_score;
                const statusLabel = document.querySelector('.text-risk-high');
                statusLabel.innerText = data.risk_status;
                
                // Dynamic Color Coding for risk status
                if(data.overall_score >= 7.0) {
                    statusLabel.style.color = '#f85149';
                } else if(data.overall_score >= 4.0) {
                    statusLabel.style.color = '#d29922';
                } else {
                    statusLabel.style.color = '#3fb950';
                }

                // 2. Update Risk Summary Table Dynamically
                const tbody = document.querySelector('tbody');
                tbody.innerHTML = ''; // Clear old static placeholder data
                
                data.packages.forEach(pkg => {
                    const row = `
                        <tr class="border-b border-default/50 hover:bg-color/50">
                            <th scope="row" class="py-4 pr-6 font-medium whitespace-nowrap">${pkg.name}</th>
                            <td class="py-4 pr-6">${pkg.type}</td>
                            <td class="py-4 pr-6 font-mono text-secondary">${pkg.version}</td>
                            <td class="py-4 pr-6 font-semibold">${pkg.risk_score}</td>
                            <td class="py-4 pr-6"><span class="text-[10px] p-1.5 px-2 bg-gray-800 font-bold rounded-full uppercase">${pkg.risk_level}</span></td>
                            <td class="py-4 pr-6 font-mono text-secondary">${pkg.issue}</td>
                            <td class="py-4">${pkg.recommendation}</td>
                        </tr>
                    `;
                    tbody.innerHTML += row;
                });

                alert("Analysis Complete!");

            } catch (error) {
                console.error("Error connecting to backend:", error);
                alert("Failed to connect to the backend server.");
            }
        });
    </script>
</body>
</html>
    
   
