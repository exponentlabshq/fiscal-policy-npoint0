# 🚀 Proposer.btc - Bitcoin Proposal Platform

A modern, beautiful web platform for Bitcoin innovators to submit proposals and connect with the community for funding and collaboration.

## 🌐 **Live Demo**

**🚀 Visit the live platform:** [https://fiscal-policy-npoint0-production.up.railway.app/](https://fiscal-policy-npoint0-production.up.railway.app/)

### **🎯 What You'll See:**

**Beautiful Landing Page** featuring:
- **Hero Section**: "Ready to Build the Future of Bitcoin?" with compelling CTA
- **Feature Highlights**: Innovation First, Community Driven, Funding Opportunities
- **Platform Statistics**: 50+ proposals, 25+ projects funded, 1000+ community members, ₿150+ total investment
- **Professional Design**: Modern gradients, smooth animations, and responsive layout

**Interactive Elements**:
- **Submit Your Proposal** button that leads to the submission form
- **Responsive navigation** that works on all devices
- **Modern UI/UX** with hover effects and smooth transitions

### **📱 Try It Out:**
1. **Visit the landing page** to see the beautiful design
2. **Click "Submit Your Proposal"** to access the submission form
3. **Navigate to `/proposals`** to see the proposals listing page
4. **Test the responsive design** on different screen sizes

## 🚀 **Deploy to Railway**

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/template/new?template=https://github.com/exponentlabshq/fiscal-policy-npoint0)

**One-click deployment to Railway** - Get your own instance running in minutes!

## ✨ **Features**

### **🎯 Landing Page**
- **Modern, responsive design** with gradient backgrounds
- **Clear value proposition** for Bitcoin proposers
- **Compelling call-to-action** to submit proposals
- **Feature highlights** showcasing platform benefits
- **Platform statistics** to build trust and credibility

### **📝 Proposal Submission System**
- **Comprehensive form** for detailed proposal submission
- **Required fields**: Title, subtitle, description, problem statement
- **Links**: GitHub repository, YouTube demo, website, email
- **Project details**: ETA, investment requirements in BTC
- **HTMX integration** for smooth form submission

### **📋 Proposal Management**
- **View all submitted proposals** in an organized list
- **Search and filter** capabilities
- **Contact information** for each proposer
- **Project status tracking**

## 🛠 **Technology Stack**

- **Backend**: Python Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Modern CSS with gradients and animations
- **Interactive Elements**: HTMX for dynamic content
- **Deployment**: Railway (production), Local development
- **Version Control**: Git with GitHub integration

## 🚀 **Quick Start**

### **Local Development**

1. **Clone the repository**
   ```bash
   git clone https://github.com/exponentlabshq/fiscal-policy-npoint0.git
   cd fiscal-policy-npoint0
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python3 app.py
   ```

4. **Open your browser**
   - Main page: http://localhost:9999/
   - Submit form: http://localhost:9999/submit
   - View proposals: http://localhost:9999/proposals

### **Production Deployment**

The application is automatically deployed to Railway from the main branch:

- **Platform**: Railway
- **URL**: https://fiscal-policy-npoint0-production.up.railway.app/
- **Auto-deploy**: Enabled (pushes to main trigger deployment)
- **Health check**: `/health` endpoint for monitoring

## 📁 **Project Structure**

```
fiscal-policy-npoint0/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── nixpacks.toml         # Railway deployment configuration
├── templates/             # HTML templates
│   ├── landing.html      # Beautiful landing page
│   ├── submit.html       # Proposal submission form
│   ├── proposals.html    # List all proposals
│   └── proposal.html     # Individual proposal view
├── test_api.py           # API testing utilities
├── test_templates.py     # Template testing utilities
└── README.md             # This file
```

## 🌟 **Key Routes**

- **`/`** - Landing page with platform introduction
- **`/submit`** - Proposal submission form
- **`/submit` (POST)** - Process proposal submission
- **`/proposals`** - View all submitted proposals
- **`/health`** - Health check endpoint for monitoring

## 🎨 **Design Features**

- **Responsive design** that works on all devices
- **Modern gradient backgrounds** with professional appearance
- **Smooth hover effects** and transitions
- **Clean typography** and spacing
- **Professional color scheme** suitable for financial applications

## 🔧 **Configuration**

### **Environment Variables**
- `PORT` - Server port (default: 9999 for local, Railway sets this automatically)

### **Railway Configuration**
- **Builder**: Railpack (Python)
- **Start Command**: `gunicorn app:app`
- **Health Check**: `/health` endpoint
- **Auto-restart**: On failure with retry logic

## 🧪 **Testing**

### **API Testing**
```bash
python3 test_api.py
```

### **Template Testing**
```bash
python3 test_templates.py
```

### **Manual Testing**
- Test form submission with sample data
- Verify proposal storage and retrieval
- Check responsive design on different screen sizes

## 🚀 **Deployment History**

This project successfully overcame several deployment challenges:

1. **Initial setup** - Basic Flask app with templates
2. **Railway configuration** - Learned Railway uses nixpacks.toml, not Procfile
3. **Port configuration** - Fixed port binding issues for Railway
4. **Production deployment** - Successfully deployed with Gunicorn WSGI server

## 🤝 **Contributing**

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 **License**

This project is open source and available under the [MIT License](LICENSE).

## 🎯 **Future Enhancements**

- **Database integration** (replace in-memory storage)
- **User authentication** and proposal management
- **Advanced search and filtering**
- **Email notifications** for proposal updates
- **Admin dashboard** for proposal review
- **Blockchain integration** for proposal funding

## 🌟 **About Proposer.btc**

Proposer.btc is designed to be the premier platform for Bitcoin innovators to:
- **Submit funding proposals** to the community
- **Connect with investors** and collaborators
- **Showcase innovative projects** in the Bitcoin ecosystem
- **Build the future** of Bitcoin technology and infrastructure

---

**Built with ❤️ for the Bitcoin community**

*Deployed and maintained by the Exponent Labs team*