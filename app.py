import json
from flask import Flask, render_template, request

from bulbs.bulbs_fill import RoomFill

app = Flask(__name__)


@app.route('/bulbs_status/', methods=['GET'])
def orders_status():
    """Get bulbs room fill
    :param request; get
    :return room: json
    """
    filename = request.args.get('filename')
    print(filename)
    room = RoomFill(filename)
    data = room.bulbs()
    return render_template('room.html', room=data)




if __name__ == '__main__':    
    app.run(debug=True)
