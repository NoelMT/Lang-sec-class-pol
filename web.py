from flask import Flask, request, jsonify, render_template_string
import json
import imp_1
app = Flask(__name__)
app.secret_key = 'some_secret_key'  # Replace with your actual secret key

class User:
    def __init__(self, name):
        self.name = name 
class profile(User):
    def __init__(self, name='some_name'):
        super().__init__(name)

def merge(src, dst):
    # Recursive merge function
    for k, v in src.items():
        if hasattr(dst, '__getitem__'):
            if dst.get(k) and type(v) == dict:
                merge(v, dst.get(k))
            else:
                dst[k] = v
        elif hasattr(dst, k) and type(v) == dict:

            merge(v, getattr(dst, k))
        else:
            #print(dst,k,v)
            setattr(dst, k, v)

@app.route('/', methods=['GET', 'POST'])
def merge_json():
    if request.method == 'POST':
        src_text = request.form.get('src')
        if src_text == "":
            #print(User)
            #print(profile)
            #print(User("n").__class__.__init__.__globals__)
            ##setattr(User("n").__class__.__init__.__globals__["app"], "secret_key", "new_key")
            new_user = User("n")
            #print(app.secret_key)
            #print(dir(new_user.__init__.__globals__["__loader__"].__module__))
            #print((new_user.__init__.__globals__["__builtins__"].__import__("imp_1").test()))
            #print(test())
            
            return ""
        else:
            try:
                src = json.loads(src_text)
            except json.JSONDecodeError:
                return jsonify({'error': 'Invalid JSON input'}), 400

            user = profile()
            merge(src, user)
            return render_template_string(f'''
                    <!doctype html>
                    <title>Merge JSON Result</title>
                    <h1>Merged JSON</h1>
                    <pre>{ print(User.__qualname__) }</pre>
                    <pre>{ app.secret_key }</pre>
                    <a href='/'>Go back</a>
                    ''')

    
    return render_template_string('''
    <!doctype html>
    <title>Merge JSON</title>
    <h1>Merge JSON Input</h1>
    <form action="/" method="post">
      <label for="src">Source JSON:</label><br>
      <textarea name="src" rows="10" cols="30"></textarea><br><br>
      <input type=submit value="Merge">
    </form>
    ''')

if __name__ == '__main__':
    app.run(debug=True)