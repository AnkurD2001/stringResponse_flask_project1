from flask import Flask

FAI=Flask(__name__)

@FAI.route('/stringResponse')
def stringResponse():
    return 'this is first stringResponse'

if __name__=='__main__':
    FAI.run(debug=True)