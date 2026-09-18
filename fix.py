with open('index.html', 'r') as f:
    content = f.read()

style_block = '''<style>
  html, body { margin: 0; padding: 0; height: 100%; width: 100%; overflow: hidden; }
  @media screen and (orientation: portrait) {
    #rotate-hint { display: flex; }
    flt-glass-pane, flutter-view { transform: rotate(90deg); transform-origin: center; width: 100vh; height: 100vw; position: absolute; top: 50%; left: 50%; margin-top: -50vw; margin-left: -50vh; }
  }
  @media screen and (orientation: landscape) {
    #rotate-hint { display: none; }
  }
  #rotate-hint { position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: black; color: white; z-index: 9999; align-items: center; justify-content: center; text-align: center; font-family: sans-serif; font-size: 18px; padding: 20px; box-sizing: border-box; }
  </style>
</head>'''

content = content.replace('</head>', style_block)

with open('index.html', 'w') as f:
    f.write(content)

print("Done!")
