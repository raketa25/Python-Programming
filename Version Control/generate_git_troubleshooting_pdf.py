"""
This Code generates a PDF troubleshooting guide for Git issues commonly faced by AI engineering students working on RAG and Ollama projects. It covers common problems, their causes, and solutions, as well as best practices for using Git in AI projects. The PDF is created using the ReportLab library and is designed to be a helpful resource for students encountering Git-related challenges in their projects.
"""

from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch

def generate_pdf(filename="Git_CI_CD_Troubleshooting_Guide.pdf"):
    doc = SimpleDocTemplate(filename, pagesize=A4, rightMargin=72, leftMargin=72,
                            topMargin=72, bottomMargin=72)
    
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle('Title', parent=styles['Title'], fontSize=18, spaceAfter=30)
    heading_style = ParagraphStyle('Heading', parent=styles['Heading2'], fontSize=14, spaceAfter=12)
    normal_style = styles['Normal']
    
    story = []
    
    # Title
    story.append(Paragraph("Version Control & CI/CD Troubleshooting Guide", title_style))
    story.append(Paragraph("For AI Engineering Students (RAG & Ollama Projects)", 
                          ParagraphStyle('Subtitle', parent=normal_style, fontSize=12, spaceAfter=30)))
    
    # Section 1: Common Git Issues on Windows
    story.append(Paragraph("1. Common Git Issues on Windows + Git Bash", heading_style))
    
    issues = [
        ["Problem", "Cause", "Solution"],
        ["'Only one usage of each socket address' when running ollama serve", "Ollama app already running in background", "Quit Ollama from system tray or kill process"],
        ["ConnectionError: Failed to connect to Ollama (localhost:11434)", "Server not running or IPv6 vs IPv4 issue in Git Bash", "Use ollama.Client(host='http://127.0.0.1:11434') or run ollama serve in PowerShell"],
        ["invalid path ... colon (:) in folder name", "Windows doesn't allow ':' in filenames (e.g. 'Intro to TCP:IPv4...')", "git config core.protectNTFS false + sparse-checkout"],
        ["fatal: destination path '.' already exists", "Trying to clone into non-empty folder", "cd to a new empty folder first"],
        ["You are in a sparse checkout...", "Using git sparse-checkout", "git sparse-checkout disable (or fix with protectNTFS)"],
        ["warning: adding embedded git repository", "Nested .git folder (e.g. rag-intro inside another repo)", "git rm --cached <folder> -r --force or copy files to clean folder"],
        ["remote origin already exists", "Trying to add remote again", "git remote set-url origin <your-url>"],
    ]
    
    t = Table(issues, colWidths=[2.2*inch, 2*inch, 2.2*inch])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.grey),
        ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0,0), (-1,0), 12),
        ('BACKGROUND', (0,1), (-1,-1), colors.beige),
        ('GRID', (0,0), (-1,-1), 1, colors.black)
    ]))
    story.append(t)
    story.append(Spacer(1, 20))
    
    # Section 2: Sparse Checkout Commands (What We Used)
    story.append(Paragraph("2. Sparse Checkout – How to Pull Only One Folder", heading_style))
    story.append(Paragraph("""
    <b>Best commands we used:</b><br/>
    1. git clone --no-checkout &lt;url&gt; .<br/>
    2. git sparse-checkout init --cone<br/>
    3. git sparse-checkout set "Folder Name"<br/>
    4. git config core.protectNTFS false   ← Important for Windows + colons<br/>
    5. git checkout
    """, normal_style))
    story.append(Spacer(1, 15))
    
    # Section 3: Fixing Remote & Pushing to Your Repo
    story.append(Paragraph("3. Connecting & Pushing to Your Own Repository", heading_style))
    story.append(Paragraph("""
    • git remote -v   → check current remotes<br/>
    • git remote set-url origin https://github.com/yourusername/yourrepo.git<br/>
    • git branch -M main<br/>
    • git push -u origin main
    """, normal_style))
    story.append(Spacer(1, 15))
    
    # Section 4: Best Practices for AI Students
    story.append(Paragraph("4. Best Practices for AI / RAG Projects", heading_style))
    story.append(Paragraph("""
    • Never commit virtual environments (AIenv, venv)<br/>
    • Use .gitignore (add __pycache__/, *.pyc, .env, venv/)<br/>
    • Keep large models & data outside Git (use .gitignore or Git LFS)<br/>
    • Run ollama serve in a separate terminal / use Ollama desktop app<br/>
    • Test embeddings with explicit Client(host='http://127.0.0.1:11434')<br/>
    • Create clean folders instead of nesting repos
    """, normal_style))
    
    story.append(Spacer(1, 30))
    story.append(Paragraph("Generated from real troubleshooting session • April 2026", 
                          ParagraphStyle('Footer', parent=normal_style, fontSize=10, alignment=1)))
    
    doc.build(story)
    print(f"✅ PDF successfully generated: {filename}")

# Run the script
if __name__ == "__main__":
    generate_pdf()