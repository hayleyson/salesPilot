# salesPilot

## Set development environment
```
$ conda create -n p4ds_team2 python=3.9
$ conda activate p4ds_team2
$ pip install -r requirements.txt
```

## Run program
### Front end
```
(p4ds_team2) $ cd frontend
(p4ds_team2) $ streamlit run app.py

  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.1.176:8501
```

### Backend
```
(p4ds_team2) $ cd backend
(p4ds_team2) $ python main.py


 * Serving Flask app 'main'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with watchdog (fsevents)

 * Debugger is active!
 * Debugger PIN: 410-538-981
```