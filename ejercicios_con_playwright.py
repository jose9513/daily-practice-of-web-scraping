from playwright.sync_api import sync_playwright

# 1. Iniciamos el motor de Playwright
with sync_playwright() as p:
    print("🤖 Despertando al bot...")
    
    # 2. Abrimos Chrome. 'headless=False' es el secreto para que TÚ puedas ver la ventana.
    navegador = p.chromium.launch(headless=False) 
    
    # 3. Abrimos una pestaña nueva
    pagina = navegador.new_page()
    
    print("🌐 Viajando a la web de frases...")
    # 4. Le decimos al navegador a dónde ir
    pagina.goto("https://quotes.toscrape.com/")
    
    print("👀 ¡Mira la pantalla! El bot cerrará esto en 3 segundos...")
    
    # 5. Hacemos que el bot espere 3 segundos (3000 milisegundos) para que te dé tiempo de verlo
    pagina.wait_for_timeout(3000) 
    
    # 6. Apagamos todo de forma limpia
    navegador.close()
    
print("🏆 Travesura completada. ¡Bienvenido a las grandes ligas!")