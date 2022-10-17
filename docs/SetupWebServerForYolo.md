## Prerequisites:

Execute command:

```
pip install -r requirements.txt
```

After that, you can start Flask Web Server using command:

```
python server.py
```

Open this [link](http://localhost:3000/test). You should get an answer "Test was successfull"

If it worked, open [predict specific image](http://localhost:3000/image?name=913_0_jpg.rf.2e6547f5d2bfe87104c6ef25f54ae86e.jpg).
You should get back the prediction details.
The first prediction request will load yolo Model, and execution will take more time.
For all next requests, prediction should be very fast.

Try replacing the image name with other images from your test folder and see the results
