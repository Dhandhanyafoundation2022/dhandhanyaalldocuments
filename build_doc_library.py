import os
import csv

# ---------------- CONFIG ----------------
DOCS_FOLDER = "docs"          # Folder jisme aapki saari files hongi
CSV_FILE = "documents.csv"    # CSV file ka naam
HTML_FILE = "index.html"      # HTML output file
COMPANY_NAME = "🚀 DHANDHANYA GROUP"
COMPANY_ADDRESS = "🏢 BB Tower, 2nd Floor, Kargi Road, Opp. Vidhya Vihar Phase 2, Dehradun, Uttarakhand 248001"
LOGO_FILE = "logo.png"        # Logo file ka naam
# ---------------------------------------

def create_csv():
    """CSV file banata hai jo sab files ka record rakhega"""
    files = os.listdir(DOCS_FOLDER)
    data = []
    for f in files:
        path = os.path.join(DOCS_FOLDER, f)
        if os.path.isfile(path):
            data.append([f, path])

    with open(CSV_FILE, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["File Name", "Path"])
        writer.writerows(data)

    print(f"✅ CSV updated/created: {CSV_FILE} ({len(data)} items)")

def get_file_icon(file):
    """Extension ke hisab se icon choose karo"""
    ext = file.lower()
    if ext.endswith(".pdf"):
        return "📕"
    elif ext.endswith(".xlsx") or ext.endswith(".csv"):
        return "📗"
    elif ext.endswith(".doc") or ext.endswith(".docx"):
        return "📘"
    elif ext.endswith(".jpg") or ext.endswith(".jpeg") or ext.endswith(".png"):
        return "🖼️"
    else:
        return "📄"

def create_html():
    """HTML UI banata hai"""
    files = os.listdir(DOCS_FOLDER)
    file_list = [f for f in files if os.path.isfile(os.path.join(DOCS_FOLDER, f))]

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>{COMPANY_NAME}</title>
  <style>
    body {{
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      margin: 0; padding: 0;
      background: linear-gradient(135deg, #0f0f0f, #232323);
      color: #fff;
    }}
    header {{
      background: #111;
      padding: 20px;
      text-align: center;
      box-shadow: 0 4px 10px rgba(0,0,0,0.4);
    }}
    header img {{
      height: 70px;
      vertical-align: middle;
      margin-right: 15px;
      border-radius: 10px;
    }}
    .company-name {{
      font-size: 36px;
      font-weight: bold;
      color: #00ffc6;
      letter-spacing: 2px;
      text-shadow: 0 0 10px #00ffc6, 0 0 20px #00ffc6;
      display: block;
      margin-top: 10px;
    }}
    .company-address {{
      font-size: 16px;
      color: #ccc;
      margin-top: 5px;
      display: block;
    }}
    .container {{
      max-width: 900px;
      margin: 30px auto;
      padding: 20px;
    }}
    .search-container {{
      position: relative;
      margin-bottom: 20px;
    }}
    input {{
      width: 100%;
      padding: 15px;
      border: none;
      border-radius: 8px;
      font-size: 18px;
      outline: none;
      box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }}
    #suggestions {{
      position: absolute;
      top: 55px;
      background: #222;
      border-radius: 8px;
      width: 100%;
      max-height: 180px;
      overflow-y: auto;
      z-index: 10;
    }}
    #suggestions div {{
      padding: 12px;
      cursor: pointer;
      border-bottom: 1px solid #333;
    }}
    #suggestions div:hover {{
      background: #00ffc6;
      color: #000;
    }}
    ul {{
      list-style: none;
      padding: 0;
    }}
    li {{
      background: #2c2c2c;
      padding: 15px;
      margin: 10px 0;
      border-radius: 10px;
      display: flex;
      align-items: center;
    }}
    li:hover {{
      background: #00ffc6;
      color: #000;
    }}
    a {{
      text-decoration: none;
      color: inherit;
      font-size: 18px;
      margin-left: 10px;
      word-break: break-all;
    }}
  </style>
</head>
<body>
  <header>
    <img src="{LOGO_FILE}" alt="Logo" onerror="this.style.display='none'">
    <span class="company-name">{COMPANY_NAME}</span>
    <span class="company-address">{COMPANY_ADDRESS}</span>
  </header>
  <div class="container">
    <div class="search-container">
      <input type="text" id="search" placeholder="Search your files..." onkeyup="filterDocs()">
      <div id="suggestions"></div>
    </div>
    <ul id="doc-list">
"""

    for f in file_list:
        icon = get_file_icon(f)
        html_content += f'      <li>{icon} <a href="{DOCS_FOLDER}/{f}" target="_blank">{f}</a></li>\n'

    html_content += """    </ul>
  </div>
  <script>
    const allFiles = """ + str(file_list) + """;

    function filterDocs() {
      let input = document.getElementById('search').value.toLowerCase();
      let items = document.querySelectorAll('#doc-list li');
      let suggestions = document.getElementById('suggestions');
      suggestions.innerHTML = '';

      items.forEach(item => {
        let text = item.textContent.toLowerCase();
        item.style.display = text.includes(input) ? '' : 'none';
      });

      if (input) {
        let matched = allFiles.filter(f => f.toLowerCase().includes(input));
        matched.slice(0, 6).forEach(f => {
          let div = document.createElement('div');
          div.textContent = f;
          div.onclick = () => {
            document.getElementById('search').value = f;
            suggestions.innerHTML = '';
            items.forEach(item => {
              item.style.display = item.textContent.includes(f) ? '' : 'none';
            });
          };
          suggestions.appendChild(div);
        });
      }
    }
  </script>
</body>
</html>
"""

    with open(HTML_FILE, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"✅ HTML file '{HTML_FILE}' created successfully!")

if __name__ == "__main__":
    create_csv()
    create_html()
