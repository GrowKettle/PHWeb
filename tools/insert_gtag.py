from pathlib import Path

GTAG = """<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-K77DLZ0QSS"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-K77DLZ0QSS');
</script>
"""

count = 0

for html in Path(".").rglob("*.html"):

    text = html.read_text(encoding="utf-8")

    if "G-K77DLZ0QSS" in text:
        continue

    if "<head>" in text:
        text = text.replace("<head>", "<head>\n\n" + GTAG + "\n", 1)
        html.write_text(text, encoding="utf-8")
        print(f"Updated: {html}")
        count += 1

print(f"\nUpdated {count} HTML files.")