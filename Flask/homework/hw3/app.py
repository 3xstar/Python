from flask import Flask, render_template, request

app = Flask(__name__)

movies = {
    1: {
        "name": "Fight Club",
        "rating": 8.5,
        "description": "Bro is fighting with Brad Pitt in his head ahh. "
                       "Первое правило шизофрении — никому не рассказывать про своего воображаемого альфа-друга, "
                       "который варит мыло, выглядит как гигачад и подговаривает тебя обнулить "
                       "кредитные истории ради фана. В итоге обычный офисный клерк, страдающий бессонницей, "
                       "случайно создаёт подпольную армию из парней, которые просто хотели выпустить пар после работы, "
                       "а получили полноценный анархо-капиталистический хаос глобального масштаба.",
        "image": "https://m.media-amazon.com/images/M/MV5BOTgyOGQ1NDItNGU3Ny00MjU3LTg2YWEtNmEyYjBiMjI1Y2M5XkEyXkFqcGc@._V1_.jpg"
    },
    2: {
        "name": "Drive",
        "rating": 7.8,
        "description": "Bro doesn't died in the end. "
                       "Реальный молчаливый сигма в куртке со скорпионом, который слушает ночной синтвейв, "
                       "зубочистку изо рта не выпускает и просто молча смотрит в душу 90% экранного времени. "
                       "Настоящий герой, буквально я. Он даёт своим клиентам ровно пять минут, "
                       "в течение которых готов прикрыть любой криминал, но если они не укладываются — "
                       "это их проблемы. Чистый эстетичный нео-нуар, где количество слов главного героя "
                       "можно пересчитать по пальцам, зато стиль выкручен на абсолютный максимум.",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSA7NIJyvslcY-eut3vOoJ55vwkptsUTAua0rST1F9Ko-JOp8F9Fk7FlwA&s=10"
    },
    3: {
        "name": "Deadpool & Wolverine",
        "rating": 7.5,
        "description": "2 stupid silly guys trying to save the world. "
                       "Один безостановочно кринжует, шутит шутки ниже пояса и ломает четвертую стену, "
                       "а второй слишком старый для этого фансервиса и просто хочет порезать кого-нибудь "
                       "своими когтями под поп-хиты нулевых. Логан максимально не понимает, куда он попал и "
                       "почему этот парень в красном трико постоянно обращается к каким-то зрителям, "
                       "пока они разносят целые таймлайны, пытаются не умереть со стыда "
                       "и спасают вселенную Disney от тотального дефолта.",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSbheZAOYsbLxi_l0LXsay1NyC9qTt_5O7uj4__9LCtHRtH9s9EAzA0ie6N&s=10"
    },
    4: {
        "name": "Spider-Man 2",
        "rating": 7.5,
        "description": "Spider-Bro is fighting against Mecha-Octopus. "
                       "У бедного пацана тотальный депрессняк, суперсилы пропадают на полшестого, "
                       "за аренду хаты платить нечем, девка ушла, а тут еще сумасшедший дед с "
                       "четырьмя железными щупальцами заставляет ловить поезда собственным лицом. "
                       "Питер Паркер буквально пытается выжить на минималку, доставляя пиццу, "
                       "пока его лучший друг мечтает отомстить Человеку-пауку, а весь Нью-Йорк считает его угрозой. "
                       "Легендарная классика, где драма с доставкой еды ощущается больнее, чем битва на крыше поезда.",
        "image": "https://m.media-amazon.com/images/M/MV5BNGQ0YTQyYTgtNWI2YS00NTE2LWJmNDItNTFlMTUwNmFlZTM0XkEyXkFqcGc@._V1_.jpg"
    }
}


@app.route("/")
def main():
    return render_template("index.html", movies=movies)


@app.route("/movie/<int:movie_id>")
def movie_page(movie_id):
    movie = movies.get(movie_id)
    return render_template('movie.html', movie_id=movie_id, movie=movie, movies=movies)

if __name__ == "__main__":
    app.run(debug=True)