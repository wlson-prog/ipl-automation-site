import requests

def update_table():
    # Replace with your actual CricAPI Key
    API_KEY = "YOUR_API_KEY" 
    # 2026 Series ID (Check CricAPI dashboard as the season starts)
    SERIES_ID = "c75f8333-2802-4297-9f93-41c88147d3c2" 
    
    url = f"https://api.cricapi.com/v1/series_points?apikey={API_KEY}&id={SERIES_ID}"
    response = requests.get(url).json()

    if response['status'] == 'success':
        html_content = '<table class="ipl-table"><tr><th>Team</th><th>P</th><th>W</th><th>Pts</th></tr>'
        for team in response['data']:
            html_content += f"<tr><td>{team['name']}</td><td>{team['m']}</td><td>{team['w']}</td><td>{team['p']}</td></tr>"
        html_content += "</table>"
        
        # Saves the table to an HTML file your site can include
        with open("points-table.html", "w") as f:
            f.write(html_content)

if __name__ == "__main__":
    update_table()
