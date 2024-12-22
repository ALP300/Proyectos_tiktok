//  Crea un juego en el que un regalo
//  está escondido detrás de una
//  serie de casillas, y el jugador 
//  debe adivinar dónde está.
// LA PERSONA HAGA 4 INTENTOS MÁXIMO
function encontrarRegalo(){
    const rangoPosiciones=5;
    const nAleatorio= Math.floor(Math.random()*rangoPosiciones);
    let intentos= 3;
    console.log("Encuenta el regalo (Elige un número del 0 al 4)");
    while(intentos>0){
        const peticion= parseInt(prompt("Ingresa un número del 0 al 4"));
        if (peticion===nAleatorio){
            console.log("ADIVINASTE, EL REGALO");
            return;
        }
        else{
            intentos--;
            console.log(
                intentos > 0
                ? `X no está ahí, te quedan ${intentos} intentos`
                : `:( Te quedaste sin intentos, suerte para la próxima`
            )

        }
    }
}
encontrarRegalo();