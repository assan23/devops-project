from flask import Flask, render_template_string, request, jsonify
import datetime

app = Flask(__name__)

# قالب HTML الرئيسي بالفرنسية
MAIN_TEMPLATE = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Application DevOps - CI/CD Pipeline</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
            min-height: 100vh;
            color: #fff;
        }
        
        .navbar {
            background: rgba(0,0,0,0.3);
            padding: 1rem 2rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
        }
        
        .logo {
            font-size: 1.5rem;
            font-weight: bold;
        }
        
        .nav-links a {
            color: white;
            text-decoration: none;
            margin-left: 1.5rem;
            padding: 0.5rem 1rem;
            border-radius: 5px;
            transition: background 0.3s;
        }
        
        .nav-links a:hover {
            background: rgba(255,255,255,0.2);
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
        }
        
        .hero {
            text-align: center;
            padding: 3rem 1rem;
            background: rgba(255,255,255,0.1);
            border-radius: 20px;
            margin-bottom: 2rem;
            backdrop-filter: blur(10px);
        }
        
        .hero h1 {
            font-size: 3rem;
            margin-bottom: 1rem;
            animation: fadeIn 1s ease-in;
        }
        
        .hero p {
            font-size: 1.2rem;
            opacity: 0.9;
        }
        
        .cards {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
            margin-top: 2rem;
        }
        
        .card {
            background: rgba(255,255,255,0.1);
            border-radius: 15px;
            padding: 1.5rem;
            backdrop-filter: blur(10px);
            transition: transform 0.3s, box-shadow 0.3s;
        }
        
        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        }
        
        .card h3 {
            margin-bottom: 1rem;
            font-size: 1.5rem;
        }
        
        .card p {
            line-height: 1.6;
            margin-bottom: 1rem;
        }
        
        .btn {
            display: inline-block;
            padding: 0.7rem 1.5rem;
            background: #ff6b6b;
            color: white;
            text-decoration: none;
            border-radius: 25px;
            border: none;
            cursor: pointer;
            transition: background 0.3s, transform 0.3s;
            font-size: 1rem;
        }
        
        .btn:hover {
            background: #ff5252;
            transform: scale(1.05);
        }
        
        .btn-secondary {
            background: #4ecdc4;
        }
        
        .btn-secondary:hover {
            background: #45b7aa;
        }
        
        .status {
            background: rgba(0,0,0,0.3);
            border-radius: 10px;
            padding: 1rem;
            margin-top: 2rem;
            text-align: center;
        }
        
        .status-badge {
            display: inline-block;
            padding: 0.3rem 0.8rem;
            background: #4caf50;
            border-radius: 20px;
            font-size: 0.9rem;
        }
        
        @keyframes fadeIn {
            from {
                opacity: 0;
                transform: translateY(20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        @media (max-width: 768px) {
            .navbar {
                flex-direction: column;
                text-align: center;
            }
            
            .nav-links {
                margin-top: 1rem;
            }
            
            .nav-links a {
                margin: 0 0.5rem;
            }
            
            .hero h1 {
                font-size: 2rem;
            }
        }
    </style>
</head>
<body>
    <nav class="navbar">
        <div class="logo">🚀 DevOps Pipeline</div>
        <div class="nav-links">
            <a href="/">Accueil</a>
            <a href="/about">À propos</a>
            <a href="/features">Fonctionnalités</a>
            <a href="/api/data">API</a>
            <a href="/contact">Contact</a>
        </div>
    </nav>
    
    <div class="container">
        <div class="hero">
            <h1>🇫🇷 Bienvenue sur l'application DevOps</h1>
            <p>Pipeline CI/CD avec Flask, Docker et GitHub Actions</p>
            <div style="margin-top: 1.5rem;">
                <a href="/features" class="btn">Découvrir</a>
                <a href="/api/data" class="btn btn-secondary">API JSON</a>
            </div>
        </div>
        
        <div class="cards">
            <div class="card">
                <h3>📦 Flask Framework</h3>
                <p>Application web légère et performante développée avec Flask, un micro-framework Python.</p>
            </div>
            <div class="card">
                <h3>🐳 Docker</h3>
                <p>Conteneurisation de l'application pour un déploiement facile et cohérent.</p>
            </div>
            <div class="card">
                <h3>⚙️ GitHub Actions</h3>
                <p>Pipeline CI/CD automatisé pour les tests, la construction et le déploiement.</p>
            </div>
        </div>
        
        <div class="status">
            <p>🟢 Statut de l'application: <span class="status-badge">En ligne</span></p>
            <p>📅 Dernière mise à jour: {{ date }}</p>
            <p>🔄 Version: 2.0.0</p>
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(MAIN_TEMPLATE, date=datetime.datetime.now().strftime("%d/%m/%Y %H:%M"))

@app.route('/about')
def about():
    return '''
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>À propos - DevOps Application</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
                min-height: 100vh;
                color: #fff;
                margin: 0;
                padding: 0;
            }
            .container {
                max-width: 800px;
                margin: 0 auto;
                padding: 2rem;
            }
            .card {
                background: rgba(255,255,255,0.1);
                border-radius: 20px;
                padding: 2rem;
                margin-top: 2rem;
                backdrop-filter: blur(10px);
            }
            h1 {
                text-align: center;
                margin-bottom: 2rem;
            }
            .nav {
                text-align: center;
                margin-top: 2rem;
            }
            .btn {
                display: inline-block;
                padding: 0.7rem 1.5rem;
                background: #ff6b6b;
                color: white;
                text-decoration: none;
                border-radius: 25px;
                margin: 0 0.5rem;
            }
            .techno {
                display: inline-block;
                background: rgba(255,255,255,0.2);
                padding: 0.3rem 0.8rem;
                border-radius: 15px;
                margin: 0.3rem;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="card">
                <h1>📖 À propos de cette application</h1>
                <p><strong>Cette application a été développée dans le cadre d'un projet DevOps.</strong></p>
                <p>Elle démontre l'utilisation des technologies modernes pour l'intégration et le déploiement continus.</p>
                
                <h3>📚 Technologies utilisées:</h3>
                <div>
                    <span class="techno">Python 3.10</span>
                    <span class="techno">Flask</span>
                    <span class="techno">Docker</span>
                    <span class="techno">GitHub Actions</span>
                    <span class="techno">Git</span>
                </div>
                
                <h3>👨‍💻 Auteur:</h3>
                <p>Assan23 - Projet DevOps</p>
                
                <h3>🎯 Objectifs:</h3>
                <ul>
                    <li>✅ Mettre en place un pipeline CI/CD</li>
                    <li>✅ Conteneuriser l'application avec Docker</li>
                    <li>✅ Automatiser les tests et le déploiement</li>
                    <li>✅ Utiliser Git pour le versionnement</li>
                </ul>
                
                <div class="nav">
                    <a href="/" class="btn">🏠 Accueil</a>
                    <a href="/features" class="btn">✨ Fonctionnalités</a>
                </div>
            </div>
        </div>
    </body>
    </html>
    '''

@app.route('/features')
def features():
    return '''
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Fonctionnalités - DevOps Application</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
                min-height: 100vh;
                color: #fff;
                margin: 0;
                padding: 0;
            }
            .container {
                max-width: 900px;
                margin: 0 auto;
                padding: 2rem;
            }
            .card {
                background: rgba(255,255,255,0.1);
                border-radius: 20px;
                padding: 2rem;
                margin-top: 2rem;
                backdrop-filter: blur(10px);
            }
            h1 { text-align: center; }
            .feature-list {
                list-style: none;
                padding: 0;
            }
            .feature-list li {
                padding: 1rem;
                margin: 1rem 0;
                background: rgba(255,255,255,0.1);
                border-radius: 10px;
                border-left: 4px solid #ff6b6b;
            }
            .btn {
                display: inline-block;
                padding: 0.7rem 1.5rem;
                background: #ff6b6b;
                color: white;
                text-decoration: none;
                border-radius: 25px;
                margin: 1rem 0.5rem 0 0;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="card">
                <h1>✨ Fonctionnalités de l'application</h1>
                <ul class="feature-list">
                    <li>🚀 <strong>Pipeline CI/CD automatisé</strong> - Tests et déploiement automatiques avec GitHub Actions</li>
                    <li>🐳 <strong>Conteneurisation Docker</strong> - Image Docker optimisée pour l'application Flask</li>
                    <li>📊 <strong>API RESTful</strong> - Endpoints JSON pour l'intégration avec d'autres services</li>
                    <li>🎨 <strong>Interface responsive</strong> - Design moderne adapté à tous les appareils</li>
                    <li>🔄 <strong>Déploiement continu</strong> - Mise à jour automatique après chaque push sur main</li>
                    <li>📝 <strong>Logging intégré</strong> - Suivi des accès et des erreurs</li>
                    <li>🔧 <strong>Configuration flexible</strong> - Variables d'environnement pour différents environnements</li>
                </ul>
                <div>
                    <a href="/" class="btn">🏠 Accueil</a>
                    <a href="/api/data" class="btn">📡 Voir l'API</a>
                </div>
            </div>
        </div>
    </body>
    </html>
    '''

@app.route('/contact')
def contact():
    return '''
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Contact - DevOps Application</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
                min-height: 100vh;
                color: #fff;
                margin: 0;
                padding: 0;
            }
            .container {
                max-width: 600px;
                margin: 0 auto;
                padding: 2rem;
            }
            .card {
                background: rgba(255,255,255,0.1);
                border-radius: 20px;
                padding: 2rem;
                margin-top: 2rem;
                backdrop-filter: blur(10px);
            }
            .info {
                margin: 1.5rem 0;
                padding: 1rem;
                background: rgba(255,255,255,0.1);
                border-radius: 10px;
            }
            .btn {
                display: inline-block;
                padding: 0.7rem 1.5rem;
                background: #ff6b6b;
                color: white;
                text-decoration: none;
                border-radius: 25px;
                margin-top: 1rem;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="card">
                <h1>📧 Contact</h1>
                <div class="info">
                    <p><strong>📱 GitHub:</strong> <a href="https://github.com/assan23" style="color: #ff6b6b;">github.com/assan23</a></p>
                    <p><strong>📁 Projet:</strong> <a href="https://github.com/assan23/devops-project" style="color: #ff6b6b;">devops-project</a></p>
                    <p><strong>🐳 Docker Hub:</strong> À venir</p>
                    <p><strong>📅 Créé le:</strong> Avril 2026</p>
                </div>
                <div style="text-align: center;">
                    <a href="/" class="btn">🏠 Retour à l'accueil</a>
                </div>
            </div>
        </div>
    </body>
    </html>
    '''

@app.route('/api/data')
def api_data():
    return jsonify({
        'application': 'DevOps Pipeline',
        'version': '2.0.0',
        'language': 'Python',
        'framework': 'Flask',
        'status': 'online',
        'features': [
            'CI/CD avec GitHub Actions',
            'Conteneurisation Docker',
            'API RESTful',
            'Interface responsive'
        ],
        'timestamp': datetime.datetime.now().isoformat(),
        'server': 'Flask Development Server'
    })

@app.route('/api/status')
def api_status():
    return jsonify({
        'status': 'healthy',
        'uptime': 'en ligne',
        'environment': 'development',
        'python_version': '3.10',
        'timestamp': datetime.datetime.now().isoformat()
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)