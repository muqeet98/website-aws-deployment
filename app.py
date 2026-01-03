from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from random import choice
from re import match
import locations

PORT = 8080

app = FastAPI()


@app.get('/favicon.ico', include_in_schema=False, status_code=204)
async def favicon():
    return True


@app.get("/", response_class=HTMLResponse)
async def index():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CI/CD Portfolio - Abdul Muqeet</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            line-height: 1.6;
            color: #333;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }

        .container {
            max-width: 900px;
            margin: 0 auto;
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            overflow: hidden;
        }

        .header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 60px 40px;
            text-align: center;
        }

        .header h1 {
            font-size: 2.5em;
            margin-bottom: 10px;
            font-weight: 700;
        }

        .header p {
            font-size: 1.2em;
            opacity: 0.9;
        }

        .content {
            padding: 40px;
        }

        .section {
            margin-bottom: 40px;
        }

        .section-title {
            font-size: 1.8em;
            color: #667eea;
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 3px solid #667eea;
            display: inline-block;
        }

        .timeline {
            position: relative;
            padding-left: 30px;
        }

        .timeline::before {
            content: '';
            position: absolute;
            left: 0;
            top: 0;
            bottom: 0;
            width: 3px;
            background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
        }

        .timeline-item {
            position: relative;
            margin-bottom: 30px;
            padding-left: 30px;
        }

        .timeline-item::before {
            content: '';
            position: absolute;
            left: -36px;
            top: 5px;
            width: 15px;
            height: 15px;
            border-radius: 50%;
            background: #667eea;
            border: 3px solid white;
            box-shadow: 0 0 0 3px #667eea;
        }

        .timeline-item h3 {
            color: #333;
            font-size: 1.3em;
            margin-bottom: 8px;
        }

        .timeline-item p {
            color: #666;
            line-height: 1.6;
        }

        .badge {
            display: inline-block;
            background: #f0f4ff;
            color: #667eea;
            padding: 5px 15px;
            border-radius: 20px;
            font-size: 0.85em;
            margin: 5px 5px 5px 0;
            font-weight: 600;
        }

        .tech-stack {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin-top: 10px;
        }

        .contact {
            background: #f8f9ff;
            padding: 30px;
            border-radius: 15px;
            text-align: center;
        }

        .contact h2 {
            color: #667eea;
            margin-bottom: 15px;
        }

        .contact a {
            color: #667eea;
            text-decoration: none;
            font-size: 1.1em;
            font-weight: 600;
            transition: all 0.3s;
        }

        .contact a:hover {
            color: #764ba2;
            text-decoration: underline;
        }

        .api-info {
            background: #fff9e6;
            border-left: 4px solid #ffc107;
            padding: 20px;
            border-radius: 5px;
            margin-top: 20px;
        }

        .api-info h3 {
            color: #f57c00;
            margin-bottom: 10px;
        }

        .api-info a {
            color: #667eea;
            text-decoration: none;
            font-weight: 600;
        }

        .api-info a:hover {
            text-decoration: underline;
        }

        @media (max-width: 768px) {
            .header h1 {
                font-size: 2em;
            }

            .content {
                padding: 30px 20px;
            }

            .section-title {
                font-size: 1.5em;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>CI/CD Portfolio</h1>
            <p>Continuous Integration & Deployment Journey</p>
        </div>

        <div class="content">
            <div class="section">
                <h2 class="section-title">My CI/CD Implementation Journey</h2>

                <div class="timeline">
                    <div class="timeline-item">
                        <h3>1. GitHub Actions Setup</h3>
                        <p>Implemented automated CI/CD pipeline using GitHub Actions for continuous integration and deployment workflows.</p>
                        <div class="tech-stack">
                            <span class="badge">GitHub Actions</span>
                            <span class="badge">YAML</span>
                            <span class="badge">Workflow Automation</span>
                        </div>
                    </div>

                    <div class="timeline-item">
                        <h3>2. Container Image Build & Test</h3>
                        <p>Created Docker containerization strategy with automated builds, testing, and image optimization for efficient deployment.</p>
                        <div class="tech-stack">
                            <span class="badge">Docker</span>
                            <span class="badge">Container Registry</span>
                            <span class="badge">Image Optimization</span>
                        </div>
                    </div>

                    <div class="timeline-item">
                        <h3>3. FastAPI Application Development</h3>
                        <p>Built a modern, high-performance RESTful API using FastAPI with automatic documentation and validation.</p>
                        <div class="tech-stack">
                            <span class="badge">Python</span>
                            <span class="badge">FastAPI</span>
                            <span class="badge">REST API</span>
                            <span class="badge">Uvicorn</span>
                        </div>
                    </div>

                    <div class="timeline-item">
                        <h3>4. AWS Infrastructure Setup</h3>
                        <p>Configured AWS cloud infrastructure for scalable application hosting and deployment automation.</p>
                        <div class="tech-stack">
                            <span class="badge">AWS</span>
                            <span class="badge">Cloud Deployment</span>
                            <span class="badge">Infrastructure as Code</span>
                        </div>
                    </div>

                    <div class="timeline-item">
                        <h3>5. Automated Testing & Quality Assurance</h3>
                        <p>Integrated automated testing pipelines to ensure code quality and reliability before deployment.</p>
                        <div class="tech-stack">
                            <span class="badge">pytest</span>
                            <span class="badge">CI Testing</span>
                            <span class="badge">Code Quality</span>
                        </div>
                    </div>

                    <div class="timeline-item">
                        <h3>6. Production Deployment</h3>
                        <p>Successfully deployed containerized applications to production with zero-downtime deployment strategies.</p>
                        <div class="tech-stack">
                            <span class="badge">Production Deploy</span>
                            <span class="badge">Monitoring</span>
                            <span class="badge">DevOps</span>
                        </div>
                    </div>
                </div>
            </div>

            <div class="api-info">
                <h3>Location Service API</h3>
                <p>This application includes a Location Service API that returns geographic data based on IP addresses.</p>
                <p style="margin-top: 10px;">
                    <strong>Try it:</strong>
                    <a href="/127.0.0.1" target="_blank">/127.0.0.1</a> |
                    <a href="/docs" target="_blank">API Docs</a> |
                    <a href="/redoc" target="_blank">ReDoc</a>
                </p>
            </div>

            <div class="section">
                <div class="contact">
                    <h2>Get In Touch</h2>
                    <p style="margin-bottom: 15px; color: #666;">Interested in discussing CI/CD, DevOps, or cloud solutions?</p>
                    <a href="mailto:khabdulmuqee98@gmail.com">khabdulmuqee98@gmail.com</a>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
"""


@app.get("/{ip_address}")
async def get_location(ip_address: str):
    # validate the IP address using a regular expression
    if not match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", ip_address):
        raise HTTPException(status_code=400, detail="Invalid IP address.")

    random_city = choice(locations.cities)

    return {"ip_address": ip_address, "location": random_city}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=PORT)
