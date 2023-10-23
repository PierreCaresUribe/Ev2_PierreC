from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

# Create your views here.
def geto(request):
    data={"info1" : "Suguru Geto (夏油傑 Getō Suguru?) es uno de los principales antagonistas de la serie manga Tokyo Metropolitan Curse Technical School y de la serie secuela, Jujutsu Kaisen. Es uno de los cuatro chamanes de Clase Especial, antiguo estudiante de Masamichi Yaga y compañero de Satoru Gojo y Shoko Ieiri."
          ,"nombre" : "Suguru Geto"
          ,"rostro": "Rostro del personaje"
          ,"habilidad" : "Manipulación de maldiciones"
          ,"perAnte" : "Satoru Gojo"
          ,"perDesp" : "Yuta Okkotsu"
          ,"linkAnte" : "/gojo"
          ,"linkDesp" : "/yuta"
          ,"1imagen" : "img/geto.jpg"
          ,"2imagen" : "img/geto_manipulacion.jpeg"
          ,"podio" : "Entre los tres Hechizeros de grado especial este queda en: "
          ,"poder": "img/tercero.png"
          }
    return render(request,"app2/app2.html",data)


def yuta(request):
    data={"info1" : "Yuta Okkotsu (乙骨憂太 Okkotsu Yūta?) es el protagonista de la serie manga Tokyo Metropolitan Curse Technical School y uno de los personajes de la serie secuela, Jujutsu Kaisen. Es uno de los cuatro chamanes de Clase Especial y estudiante de segundo año del Colegio Técnico de Magia Metropolitana de Tokio, compañero de Maki Zenin, Panda y Toge Inumaki. Se encontraba en una misión con Miguel en Kenia[4], pero tras el incidente en Shibuya, regresó a Japón."
          ,"nombre" : "Yuta Okkotsu"
          ,"rostro": "Rostro del personaje"
          ,"habilidad" : "Mimetismo"
          ,"perAnte" : "Suguru Geto"
          ,"perDesp" : "Satoru Gojo"
          ,"linkAnte" : "/geto"
          ,"linkDesp" : "/gojo"
          ,"1imagen" : "img/yuta.jpg"
          ,"2imagen" : "img/yuta_mimetismo.jpg"
          ,"podio" : "Entre los tres Hechizeros de grado especial este queda en: "
          ,"poder":"img/segundo.png"
          }
    return render(request,"app2/app2.html",data)


def gojo(request):
    data={"info1" : "Suguru Geto (夏油傑 Getō Suguru?) es uno de los principales antagonistas de la serie manga Tokyo Metropolitan Curse Technical School y de la serie secuela, Jujutsu Kaisen. Es uno de los cuatro chamanes de Clase Especial, antiguo estudiante de Masamichi Yaga y compañero de Satoru Gojo y Shoko Ieiri."
          ,"nombre" : "Satoru Gojo"
          ,"rostro": "Rostro del personaje"
          ,"habilidad" : "Vacio Infinito"
          ,"perAnte" : "Yuta Okkotsu"
          ,"perDesp" : "Suguru Geto"
          ,"linkAnte" : "/yuta"
          ,"linkDesp" : "/geto"
          ,"1imagen" : "img/gojo.jpg"
          ,"2imagen" : "img/gojo_vacio.jpg"
          ,"podio" : "Entre los tres Hechizeros de grado especial este queda en: "
          ,"poder":"img/primero.png"
          }
    return render(request,"app2/app2.html",data)
