console.log("HOLA DESDE ARCHIVO JS en STATIC");
//let semanas=Array.from({length: 52}, (v, i) => i+1);
//let periodo1=semanas.slice(0,3);

function fechaActual() {
    hoy=new Date(Date.now())
    dia=hoy.getDate()
    mes=hoy.getMonth()+1
    año=hoy.getFullYear()
    fecha_hoy=año+'-'+mes+'-'+dia
    console.log(fecha_hoy)
    document.getElementById('txtFechaIngreso').value=(fecha_hoy)
}

let v_enfermos; 
let t_ataque;

function dia_del_año(x){
    let dia_elegido = new Date(x)
    var inicio_año=new Date("2022-01-01")
    var resta_dias=(dia_elegido.getTime() + 18000000)-inicio_año.getTime()
    var dia_del_año = Math.ceil(resta_dias/ (24*60*60*1000))
    console.log(dia_del_año)
    return(dia_del_año)
}

function calcularSemanaLoad(){
      input=document.getElementById('txtFechaIngreso')
      numero_de_dia=dia_del_año(input.value)
      console.log(numero_de_dia)
      dia_efectivo=numero_de_dia-1
      console.log(dia_efectivo)
      dia_espectacular=Math.ceil(dia_efectivo/7)
      console.log(dia_espectacular)
      periodo=Math.ceil(dia_espectacular/4)
      document.getElementById("txtSemana").value=dia_espectacular;
      document.getElementById("txtPeriodo").value=periodo;
    }


function calcularSemana(input){
    let id = input.id;
    if (id == "txtFechaIngreso"){
      numero_de_dia=dia_del_año(input.value)
      console.log(numero_de_dia)
      dia_efectivo=numero_de_dia-1
      console.log(dia_efectivo)
      dia_espectacular=Math.ceil(dia_efectivo/7)
      console.log(dia_espectacular)
      periodo=Math.ceil(dia_espectacular/4)
      document.getElementById("txtSemana").value=dia_espectacular;
      document.getElementById("txtPeriodo").value=periodo;
    }
}


function traerEnfermos(input){
    if (input.id == "txtNumeroEnfermos"){
     v_enfermos=input.value
    }
    calcularTasaAtaque(document.getElementById("txtNumeroExpuestos"))

}

function calcularTasaAtaque(input){
    if (input.id == "txtNumeroExpuestos"){
        if (input.value==""){
        t_ataque=0
        }else{
        t_ataque=v_enfermos/input.value
        }
        if(document.getElementById("txtNumeroEnfermos").value==""){
        document.getElementById("txtTasaAtaque").value=0
        }
        else{
        document.getElementById("txtTasaAtaque").value=t_ataque
        }
    }

}


window.onload=fechaActual();
window.onload=calcularSemanaLoad();
