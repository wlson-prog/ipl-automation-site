import requests
import os

def update_table():
    # Replace with your actual key from cricapi.com
    API_KEY = "YOUR_API_KEY" 
    # Current ID for IPL 2026 (Check your CricAPI dashboard)
    SERIES_ID = "c75f8333-2802-4297-9f93-41c88147d3c2" 
    
    url = f"https://api.cricapi.com/v1/series_points?apikey={API_KEY}&id={SERIES_ID}"
    
    try:
        response = requests.get(url)
        data = response.json()

        if data.get('status') == 'success' and 'data' in data:
            html_content = '<table class="ipl-table"><tr><th>Team</th><th>P</th><th>W</th><th>Pts</th></tr>'
            for team in data['data']:
                html_content += f"<tr><td>{team['name']}</td><td>{team['m']}</td><td>{team['w']}</td><td>{team['p']}</td></tr>"
            html_content += "</table>"
        else:
            # If API fails, create a placeholder so the GitHub Action doesn't error out
            print("API Match not found. Creating placeholder.")
            html_content = "<p>IPL 2026 Standings will appear here once the season starts on March 26!</p>"
            
        with open("points-table.html", "w") as f:
            f.write(html_content)
            
    except Exception as e:
        # Emergency backup file to prevent the 'pathspec' error
        with open("points-table.html", "w") as f:
            f.write("<p>Update in progress...</p>")
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    update_table()
