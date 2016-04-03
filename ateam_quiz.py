from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

name_dict = {
    'oohigashi': '大東 祐太',
    'murabayashi': '村林 巧',
    'yasui': '安井 岳',
    'ishiguro': '石黒 有晟',
    'kawai': '河合 雅',
    'koiwa': '小岩 穂菜美',
    'kouno': '河野 光志',
    'maruichi': '丸一 智加',
}

# @app.route("/")
# def hello():
#     return "Hello World!!!!!"

@app.route("/")
def welcome():
    return render_template('welcome.html')

@app.route("/web/quiz", methods=['GET', 'POST'])
def quiz_web():
    return render_template('quiz_web.html')

@app.route("/sogo/quiz", methods=['GET', 'POST'])
def quiz_sogo():
    return render_template('quiz_sogo.html')

@app.route("/web/ans", methods=['GET', 'POST'])
def ans_web():
    ans_list = ('yasui', 'oohigashi', 'murabayashi')
    user_ans_dict = dict(request.form)

    print(user_ans_dict)
    results = ans_check(ans_list, user_ans_dict)
    print(results)
    return render_template('ans_web.html',
                           correct_num=results.count('◯'),
                           ans1=name_dict[user_ans_dict['answer1'][0]],
                           ans2=name_dict[user_ans_dict['answer2'][0]],
                           ans3=name_dict[user_ans_dict['answer3'][0]],
                           result1=results[0],
                           result2=results[1],
                           result3=results[2],
                       )

@app.route("/sogo/ans", methods=['GET', 'POST'])
def ans_sogo():
    ans_list = ('kawai', 'ishiguro', 'kouno', 'koiwa', 'maruichi')
    user_ans_dict = dict(request.form)

    print(user_ans_dict)
    results = ans_check(ans_list, user_ans_dict)
    print(results)
    return render_template('ans_sogo.html',
                           correct_num=results.count('◯'),
                           ans1=name_dict[user_ans_dict['answer1'][0]],
                           ans2=name_dict[user_ans_dict['answer2'][0]],
                           ans3=name_dict[user_ans_dict['answer3'][0]],
                           ans4=name_dict[user_ans_dict['answer4'][0]],
                           ans5=name_dict[user_ans_dict['answer5'][0]],
                           result1=results[0],
                           result2=results[1],
                           result3=results[2],
                           result4=results[3],
                           result5=results[4],
                       )


def ans_check(ans, user_ans):
    results = []
    for i in range(len(ans)):
        if  ans[i] == user_ans['answer' + str(i + 1)][0]:
            results.append('◯')
        else:
            results.append('×')

    return results


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
