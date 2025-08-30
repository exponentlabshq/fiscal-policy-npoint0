# 🚂 Railway DevOps Best Practices for Python/Flask Apps

*Lessons learned from deploying Proposer.btc to Railway - A comprehensive guide to avoid deployment pitfalls*

## 🚨 **Critical Lessons Learned**

### **1. Railway Uses Nixpacks, NOT Procfile**

**❌ What We Tried (Wrong):**
```bash
# Procfile - Railway doesn't use this!
web: gunicorn wsgi:app
web: python3 app.py
web: waitress-serve --host=0.0.0.0 --port=$PORT wsgi:app
```

**✅ What Railway Actually Expects:**
```toml
# nixpacks.toml - Railway's native configuration
[build]
builder = "railpack"

[start]
cmd = "gunicorn app:app"
```

**💡 Key Insight:** Railway is NOT Heroku. Don't assume Heroku patterns work.

### **2. Port Configuration is Critical**

**❌ What We Tried (Wrong):**
```python
# app.py - Wrong port binding
app.run(debug=True, port=9999)  # Hardcoded port
app.run(host='127.0.0.1', port=9999)  # Wrong host
```

**✅ What Railway Actually Expects:**
```python
# app.py - Correct Railway configuration
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))  # Use Railway's PORT env var
    app.run(host='0.0.0.0', port=port)  # Bind to all interfaces
```

**💡 Key Insight:** Railway sets `PORT` environment variable. Use it, don't fight it.

### **3. WSGI Server is Required for Production**

**❌ What We Tried (Wrong):**
```python
# app.py - Development server won't work in production
app.run(debug=True, host='0.0.0.0', port=port)
```

**✅ What Railway Actually Expects:**
```toml
# nixpacks.toml - Production WSGI server
[start]
cmd = "gunicorn app:app"
```

**💡 Key Insight:** Flask dev server is for development only. Use Gunicorn for production.

### **4. File Structure Matters**

**❌ What We Tried (Wrong):**
```
app.py
wsgi.py          # Unnecessary complexity
Procfile         # Railway doesn't use this
```

**✅ What Railway Actually Expects:**
```
app.py           # Main Flask app
nixpacks.toml   # Railway configuration
requirements.txt # Dependencies
```

**💡 Key Insight:** Keep it simple. Railway expects direct app reference, not WSGI files.

## 🚀 **Correct Railway Setup for Python/Flask**

### **1. Project Structure**
```
your-flask-app/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── nixpacks.toml         # Railway configuration
├── templates/             # HTML templates
└── README.md             # Documentation
```

### **2. nixpacks.toml (Railway Configuration)**
```toml
[build]
builder = "railpack"

[start]
cmd = "gunicorn app:app"
```

### **3. requirements.txt**
```txt
Flask==3.0.0
gunicorn==21.2.0
```

### **4. app.py (Flask Application)**
```python
from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/health')
def health():
    return {"status": "healthy"}

if __name__ == '__main__':
    # Railway sets PORT environment variable
    port = int(os.environ.get('PORT', 8080))
    # Bind to all interfaces (required for Railway)
    app.run(host='0.0.0.0', port=port)
```

## 🔧 **Railway-Specific Best Practices**

### **1. Environment Variables**
- **Always use `os.environ.get('PORT', default_port)`** for port configuration
- **Never hardcode ports** - Railway assigns them dynamically
- **Use `0.0.0.0` as host** - Required for Railway's networking

### **2. Dependencies**
- **Include gunicorn** in requirements.txt for production WSGI server
- **Keep requirements minimal** - Only what you actually need
- **Specify versions** to avoid deployment inconsistencies

### **3. Health Checks**
- **Implement `/health` endpoint** for Railway monitoring
- **Return JSON response** for easy parsing
- **Keep it lightweight** - Don't do heavy operations

### **4. Logging and Debugging**
- **Disable debug mode** in production
- **Add print statements** for deployment debugging
- **Check Railway logs** for startup issues

## 🚨 **Common Pitfalls to Avoid**

### **1. Don't Assume Heroku Patterns**
- ❌ Procfile
- ❌ wsgi.py files
- ❌ Heroku-specific environment variables

### **2. Don't Fight Railway's Port Assignment**
- ❌ Hardcoded ports
- ❌ Ignoring PORT environment variable
- ❌ Wrong host binding

### **3. Don't Use Development Server in Production**
- ❌ `app.run()` with debug=True
- ❌ Flask development server
- ❌ Missing WSGI server

### **4. Don't Overcomplicate the Setup**
- ❌ Multiple WSGI files
- ❌ Complex deployment scripts
- ❌ Unnecessary configuration files

## 🎯 **Deployment Checklist**

### **Before Pushing to GitHub:**
- [ ] **nixpacks.toml** exists and is correct
- [ ] **requirements.txt** includes gunicorn
- [ ] **app.py** uses `0.0.0.0` and `os.environ.get('PORT')`
- [ ] **No Procfile** (Railway doesn't use it)
- [ ] **No wsgi.py** (unnecessary complexity)
- [ ] **Health endpoint** implemented at `/health`

### **After Railway Deployment:**
- [ ] **Check build logs** for any errors
- [ ] **Verify startup logs** show correct port binding
- [ ] **Test health endpoint** internally
- [ ] **Test external access** to main routes
- [ ] **Monitor for 502 errors** (indicates startup issues)

## 🤖 **System Prompt for Future Deployments**

```
You are deploying a Python Flask application to Railway. Follow these CRITICAL rules:

1. **Railway Configuration**: Use nixpacks.toml, NOT Procfile
2. **Port Binding**: Always use os.environ.get('PORT', default_port) and host='0.0.0.0'
3. **WSGI Server**: Use gunicorn for production, never Flask dev server
4. **File Structure**: Keep it simple - app.py, nixpacks.toml, requirements.txt
5. **Dependencies**: Include gunicorn in requirements.txt
6. **Health Check**: Implement /health endpoint for monitoring

NEVER use:
- Procfile (Heroku pattern)
- wsgi.py files (unnecessary)
- Hardcoded ports
- Flask development server in production
- 127.0.0.1 or localhost as host

ALWAYS use:
- nixpacks.toml for Railway configuration
- gunicorn app:app as start command
- 0.0.0.0 as host binding
- PORT environment variable for port
- Simple, direct app reference

Remember: Railway is NOT Heroku. Don't assume Heroku patterns work.
```

## 📚 **Reference Links**

- **Railway Flask Documentation**: [Railway Flask Guide](https://docs.railway.app/deploy/deployments)
- **Nixpacks Configuration**: [Nixpacks Docs](https://docs.railway.app/deploy/nixpacks)
- **Python Deployment**: [Railway Python Guide](https://docs.railway.app/deploy/deployments/python)

## 🎉 **Success Metrics**

Your Railway deployment is successful when:
- ✅ **Build completes** without errors
- ✅ **Container starts** and shows correct port binding
- ✅ **Health check passes** internally
- ✅ **External requests work** (no 502 errors)
- ✅ **All routes respond** correctly
- ✅ **Logs show** gunicorn running on correct port

## 🚀 **Quick Recovery from 502 Errors**

If you get "Application failed to respond" errors:

1. **Check Railway logs** for startup failures
2. **Verify port binding** in startup logs
3. **Confirm nixpacks.toml** is being used
4. **Check requirements.txt** includes gunicorn
5. **Verify app.py** uses correct host/port configuration
6. **Look for Python import errors** in build logs

---

**Remember**: Railway deployment is different from other platforms. Follow these practices, and you'll avoid the deployment nightmares we experienced! 🚂✨
