import requests
import os

def update_table():
    # 1. Setup API Details
    API_KEY = "YOUR_API_KEY" # Replace with your CricAPI key
    # Updated ID for IPL 2026 (Verify this in your CricAPI dashboard)
    SERIES_ID = "c75f8333-2802-4297-9f93-41c88147d3c2" 
    
    url = f"https://api.cricapi.com/v1/series_points?apikey={API_KEY}&id={SERIES_ID}"
    
    try:
        response = requests.get(url)
        data = response.json()

        if data.get('status') == 'success':
            # 2. Build the HTML content
            html_content = """
            <table class="ipl-table">
                <thead>
                    <tr><th>Team</th><th>Matches</th><th>Wins</th><th>Pts</th></tr>
                </thead>
                <tbody>
            """
            for team in data['data']:
                html_content += f"<tr><td>{team['name']}</td><td>{team['m']}</td><td>{team['w']}</td><td>{team['p']}</td></tr>"
            
            html_content += "</tbody></table>"
            
            # 3. CRITICAL STEP: Create the file
            # This writes the file to the current folder in GitHub
            with open("points-table.html", "w") as f:
                f.write(html_content)
            print("Successfully created points-table.html")
        else:
            print("API Error:", data.get('reason'))
            
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    update_table()
