from selenium import webdriver

class selenium:

    def VerificarTitulo():
        driver_path = 'path/to/chromedriver';
        driver = webdriver.Chrome(executable.path=driver_path);
        driver.get("https://www.coordenadas-gps.com/");
        WebElemento element = driver.findElement(By.id("address"));
        element.sendKeys("Universidad Politécnica de Valencia");
        element.submit();
    
    
        WebDriverWait waiting = new WebDriverWait(driver,9);
        waiting.until(ExpectedConditions.pre3senceOfeElementLocated(By.id("address")));
        
        if(driver.getTitle().equals("Universidad Politécnica de Valencia-Buscar con Google"))
            System.out.println("PASA");
        else System.err.println("FALLLA");
    
        driver.quit();
