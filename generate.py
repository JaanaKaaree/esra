from flask import Flask, render_template
from flask_frozen import Freezer
from datetime import datetime
import os

app = Flask(__name__)
app.config['FREEZER_DESTINATION'] = 'output'
app.config['FREEZER_RELATIVE_URLS'] = True
freezer = Freezer(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/business-services.html')
def business_services():
    return render_template('business-services.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

@app.route('/test-contact.html')
def test_contact():
    return render_template('test-contact.html')

@app.route('/getting-started.html')
def getting_started():
    return render_template('getting-started.html')

@app.route('/training-services.html')
def training_services():
    return render_template('training-services.html')

@app.route('/ideas-to-stories.html')
def ideas_to_stories():
    return render_template('ideas-to-stories.html')

@app.route('/bot-builder.html')
def bot_builder():
    return render_template('bot-builder.html')

@app.route('/smart-business.html')
def smart_business():
    return render_template('smart-business.html')

@app.route('/ai-business-playbook.html')
def ai_business_playbook():
    return render_template('ai-business-playbook.html')

@app.route('/ai-for-podcast.html')
def ai_for_podcast():
    return render_template('ai-for-podcast.html')

@app.route('/ai-for-video.html')
def ai_for_video():
    return render_template('ai-for-video.html')

@app.route('/cto-as-a-service.html')
def cto_as_a_service():
    return render_template('cto-as-a-service.html')

@app.route('/blog/ai-basics.html')
def blog_ai_basics():
    return render_template('blog-ai-basics.html')

@app.route('/blog/ai-specificity.html')
def blog_ai_specificity():
    return render_template('blog-ai-specificity.html')

@app.route('/blog/ai-inside.html')
def blog_ai_inside():
    return render_template('blog-ai-inside.html')

@app.route('/blog/ai-context.html')
def blog_ai_context():
    return render_template('blog-ai-context.html')

@app.route('/blog/ai-toolbox.html')
def blog_ai_toolbox():
    return render_template('blog-ai-toolbox.html')

@app.route('/blog/ai-show-dont-tell.html')
def blog_ai_show_dont_tell():
    return render_template('blog-ai-show-dont-tell.html')

@app.route('/blog/ai-workflow.html')
def blog_ai_workflow():
    return render_template('blog-ai-workflow.html')

@app.route('/blog/ai-ecosystem.html')
def blog_ai_ecosystem():
    return render_template('blog-ai-ecosystem.html')

@app.route('/blog/ai-agents.html')
def blog_ai_agents():
    return render_template('blog-ai-agents.html')

@app.route('/blog/ai-memory.html')
def blog_ai_memory():
    return render_template('blog-ai-memory.html')

@app.route('/blog/ai-collaboration.html')
def blog_ai_collaboration():
    return render_template('blog-ai-collaboration.html')

@app.route('/blog/ai-limitations.html')
def blog_ai_limitations():
    return render_template('blog-ai-limitations.html')

@app.route('/blog/ai-reasoning.html')
def blog_ai_reasoning():
    return render_template('blog-ai-reasoning.html')

@app.route('/blog/ai-multimodal.html')
def blog_ai_multimodal():
    return render_template('blog-ai-multimodal.html')

@app.route('/blog/ai-fine-tuning.html')
def blog_ai_fine_tuning():
    return render_template('blog-ai-fine-tuning.html')

@app.route('/blog/ai-rag.html')
def blog_ai_rag():
    return render_template('blog-ai-rag.html')

@app.route('/blog/ai-enterprise.html')
def blog_ai_enterprise():
    return render_template('blog-ai-enterprise.html')

@app.route('/blog/')
def blog_index():
    return render_template('blog-index.html')

def generate_sitemap():
    """Generate sitemap.xml with all routes and current date"""
    current_date = datetime.now().strftime('%Y-%m-%d')
    
    # Define all routes with their priorities and change frequencies
    routes = [
        # Main Pages
        {'url': '/', 'priority': '1.0', 'changefreq': 'weekly'},
        {'url': '/ai-business-playbook.html', 'priority': '0.8', 'changefreq': 'monthly'},
        {'url': '/ai-for-video.html', 'priority': '0.8', 'changefreq': 'monthly'},
        {'url': '/ai-for-podcast.html', 'priority': '0.8', 'changefreq': 'monthly'},
        {'url': '/cto-as-a-service.html', 'priority': '0.9', 'changefreq': 'monthly'},
        {'url': '/smart-business.html', 'priority': '0.8', 'changefreq': 'monthly'},
        {'url': '/bot-builder.html', 'priority': '0.8', 'changefreq': 'monthly'},
        {'url': '/ideas-to-stories.html', 'priority': '0.8', 'changefreq': 'monthly'},
        {'url': '/training-services.html', 'priority': '0.8', 'changefreq': 'monthly'},
        {'url': '/getting-started.html', 'priority': '0.8', 'changefreq': 'monthly'},
        {'url': '/business-services.html', 'priority': '0.8', 'changefreq': 'monthly'},
        {'url': '/contact.html', 'priority': '0.7', 'changefreq': 'monthly'},
        {'url': '/test-contact.html', 'priority': '0.5', 'changefreq': 'monthly'},
        
        # Blog Pages
        {'url': '/blog/', 'priority': '0.9', 'changefreq': 'weekly'},
        {'url': '/blog/ai-enterprise.html', 'priority': '0.7', 'changefreq': 'monthly'},
        {'url': '/blog/ai-rag.html', 'priority': '0.7', 'changefreq': 'monthly'},
        {'url': '/blog/ai-fine-tuning.html', 'priority': '0.7', 'changefreq': 'monthly'},
        {'url': '/blog/ai-multimodal.html', 'priority': '0.7', 'changefreq': 'monthly'},
        {'url': '/blog/ai-reasoning.html', 'priority': '0.7', 'changefreq': 'monthly'},
        {'url': '/blog/ai-limitations.html', 'priority': '0.7', 'changefreq': 'monthly'},
        {'url': '/blog/ai-collaboration.html', 'priority': '0.7', 'changefreq': 'monthly'},
        {'url': '/blog/ai-memory.html', 'priority': '0.7', 'changefreq': 'monthly'},
        {'url': '/blog/ai-agents.html', 'priority': '0.7', 'changefreq': 'monthly'},
        {'url': '/blog/ai-ecosystem.html', 'priority': '0.7', 'changefreq': 'monthly'},
        {'url': '/blog/ai-workflow.html', 'priority': '0.7', 'changefreq': 'monthly'},
        {'url': '/blog/ai-show-dont-tell.html', 'priority': '0.7', 'changefreq': 'monthly'},
        {'url': '/blog/ai-toolbox.html', 'priority': '0.7', 'changefreq': 'monthly'},
        {'url': '/blog/ai-context.html', 'priority': '0.7', 'changefreq': 'monthly'},
        {'url': '/blog/ai-inside.html', 'priority': '0.7', 'changefreq': 'monthly'},
        {'url': '/blog/ai-specificity.html', 'priority': '0.7', 'changefreq': 'monthly'},
        {'url': '/blog/ai-basics.html', 'priority': '0.7', 'changefreq': 'monthly'},
    ]
    
    sitemap_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
    sitemap_content += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    
    for route in routes:
        sitemap_content += f'  <url>\n'
        sitemap_content += f'    <loc>https://esra.co.nz{route["url"]}</loc>\n'
        sitemap_content += f'    <lastmod>{current_date}</lastmod>\n'
        sitemap_content += f'    <changefreq>{route["changefreq"]}</changefreq>\n'
        sitemap_content += f'    <priority>{route["priority"]}</priority>\n'
        sitemap_content += f'  </url>\n'
    
    sitemap_content += '</urlset>'
    
    # Write sitemap to output directory
    sitemap_path = os.path.join('output', 'sitemap.xml')
    with open(sitemap_path, 'w', encoding='utf-8') as f:
        f.write(sitemap_content)
    
    print(f"Sitemap generated: {sitemap_path}")

def generate_homepage():
    """Generate only the homepage (index.html)"""
    print("Generating homepage...")
    
    # Use the main app but create a custom freezer that only processes the index route
    class HomepageOnlyFreezer(Freezer):
        def freeze_yield(self):
            # Only yield the index page
            page = self._build_one('/', None)
            yield page
        
        def freeze(self):
            # Override freeze to handle the custom yield and copy static files
            pages = list(self.freeze_yield())
            
            # Copy static files
            import shutil
            static_source = 'static'
            static_dest = os.path.join('output', 'static')
            
            if os.path.exists(static_dest):
                shutil.rmtree(static_dest)
            shutil.copytree(static_source, static_dest)
            print("Static files copied successfully!")
            
            return set(page.url for page in pages if hasattr(page, 'url'))
    
    homepage_freezer = HomepageOnlyFreezer(app)
    homepage_freezer.freeze()
    print("Homepage generated successfully!")

def generate_homepage_only():
    """Generate only the homepage (index.html) - minimal approach"""
    print("Generating homepage only...")
    
    # Use the main app but only freeze the index route
    from flask_frozen import Freezer
    
    # Create a custom freezer that only processes the index route
    class SinglePageFreezer(Freezer):
        def freeze_yield(self):
            # Only yield the index page
            yield self._build_one('/', None)
    
    single_freezer = SinglePageFreezer(app)
    single_freezer.freeze()
    print("Homepage generated successfully!")

def generate_all_blog_pages():
    """Generate all blog pages"""
    print("Generating all blog pages...")
    
    # Create a temporary freezer with only blog routes
    temp_app = Flask(__name__)
    temp_app.config['FREEZER_DESTINATION'] = 'output'
    temp_app.config['FREEZER_RELATIVE_URLS'] = True
    
    # Add all blog routes
    @temp_app.route('/blog/')
    def temp_blog_index():
        return render_template('blog-index.html')
    
    @temp_app.route('/blog/ai-basics.html')
    def temp_blog_ai_basics():
        return render_template('blog-ai-basics.html')
    
    @temp_app.route('/blog/ai-specificity.html')
    def temp_blog_ai_specificity():
        return render_template('blog-ai-specificity.html')
    
    @temp_app.route('/blog/ai-inside.html')
    def temp_blog_ai_inside():
        return render_template('blog-ai-inside.html')
    
    @temp_app.route('/blog/ai-context.html')
    def temp_blog_ai_context():
        return render_template('blog-ai-context.html')
    
    @temp_app.route('/blog/ai-toolbox.html')
    def temp_blog_ai_toolbox():
        return render_template('blog-ai-toolbox.html')
    
    @temp_app.route('/blog/ai-show-dont-tell.html')
    def temp_blog_ai_show_dont_tell():
        return render_template('blog-ai-show-dont-tell.html')
    
    @temp_app.route('/blog/ai-workflow.html')
    def temp_blog_ai_workflow():
        return render_template('blog-ai-workflow.html')
    
    @temp_app.route('/blog/ai-ecosystem.html')
    def temp_blog_ai_ecosystem():
        return render_template('blog-ai-ecosystem.html')
    
    @temp_app.route('/blog/ai-agents.html')
    def temp_blog_ai_agents():
        return render_template('blog-ai-agents.html')
    
    @temp_app.route('/blog/ai-memory.html')
    def temp_blog_ai_memory():
        return render_template('blog-ai-memory.html')
    
    @temp_app.route('/blog/ai-collaboration.html')
    def temp_blog_ai_collaboration():
        return render_template('blog-ai-collaboration.html')
    
    @temp_app.route('/blog/ai-limitations.html')
    def temp_blog_ai_limitations():
        return render_template('blog-ai-limitations.html')
    
    @temp_app.route('/blog/ai-reasoning.html')
    def temp_blog_ai_reasoning():
        return render_template('blog-ai-reasoning.html')
    
    @temp_app.route('/blog/ai-multimodal.html')
    def temp_blog_ai_multimodal():
        return render_template('blog-ai-multimodal.html')
    
    @temp_app.route('/blog/ai-fine-tuning.html')
    def temp_blog_ai_fine_tuning():
        return render_template('blog-ai-fine-tuning.html')
    
    @temp_app.route('/blog/ai-rag.html')
    def temp_blog_ai_rag():
        return render_template('blog-ai-rag.html')
    
    @temp_app.route('/blog/ai-enterprise.html')
    def temp_blog_ai_enterprise():
        return render_template('blog-ai-enterprise.html')
    
    temp_freezer = Freezer(temp_app)
    temp_freezer.freeze()
    print("All blog pages generated successfully!")

def generate_specific_blog_page(template_name):
    """Generate a specific blog page by template name
    
    Args:
        template_name (str): The template name (e.g., 'blog-ai-basics', 'blog-ai-rag')
    """
    print(f"Generating specific blog page: {template_name}")
    
    # Validate template name
    if not template_name.startswith('blog-'):
        print("Error: Template name must start with 'blog-'")
        return
    
    # Create a temporary freezer with only the specific blog route
    temp_app = Flask(__name__)
    temp_app.config['FREEZER_DESTINATION'] = 'output'
    temp_app.config['FREEZER_RELATIVE_URLS'] = True
    
    # Convert template name to route
    route_path = f'/blog/{template_name.replace("blog-", "")}.html'
    
    # Create dynamic route function
    def create_route_func(template):
        def route_func():
            return render_template(template)
        return route_func
    
    # Add the specific route
    temp_app.add_url_rule(route_path, f'temp_{template_name}', create_route_func(f'{template_name}.html'))
    
    temp_freezer = Freezer(temp_app)
    temp_freezer.freeze()
    print(f"Blog page {template_name} generated successfully at {route_path}!")

def generate_main_pages():
    """Generate all main pages (non-blog pages)"""
    print("Generating all main pages...")
    
    # Create a temporary freezer with only main page routes
    temp_app = Flask(__name__)
    temp_app.config['FREEZER_DESTINATION'] = 'output'
    temp_app.config['FREEZER_RELATIVE_URLS'] = True
    
    # Add all main page routes
    @temp_app.route('/')
    def temp_index():
        return render_template('index.html')
    
    @temp_app.route('/business-services.html')
    def temp_business_services():
        return render_template('business-services.html')
    
    @temp_app.route('/contact.html')
    def temp_contact():
        return render_template('contact.html')
    
    @temp_app.route('/test-contact.html')
    def temp_test_contact():
        return render_template('test-contact.html')
    
    @temp_app.route('/getting-started.html')
    def temp_getting_started():
        return render_template('getting-started.html')
    
    @temp_app.route('/training-services.html')
    def temp_training_services():
        return render_template('training-services.html')
    
    @temp_app.route('/ideas-to-stories.html')
    def temp_ideas_to_stories():
        return render_template('ideas-to-stories.html')
    
    @temp_app.route('/bot-builder.html')
    def temp_bot_builder():
        return render_template('bot-builder.html')
    
    @temp_app.route('/smart-business.html')
    def temp_smart_business():
        return render_template('smart-business.html')
    
    @temp_app.route('/ai-business-playbook.html')
    def temp_ai_business_playbook():
        return render_template('ai-business-playbook.html')
    
    @temp_app.route('/ai-for-podcast.html')
    def temp_ai_for_podcast():
        return render_template('ai-for-podcast.html')
    
    @temp_app.route('/ai-for-video.html')
    def temp_ai_for_video():
        return render_template('ai-for-video.html')
    
    @temp_app.route('/cto-as-a-service.html')
    def temp_cto_as_a_service():
        return render_template('cto-as-a-service.html')
    
    temp_freezer = Freezer(temp_app)
    temp_freezer.freeze()
    print("All main pages generated successfully!")

def generate_whole_website():
    """Generate the complete website (all pages + sitemap)"""
    print("Generating complete website...")
    
    # Freeze the entire site
    freezer.freeze()
    print("All pages generated successfully!")
    
    # Generate sitemap
    generate_sitemap()
    print("Complete website generation finished!")

def generate_specific_page(page_name):
    """Generate a specific page by name without deleting other files
    
    Args:
        page_name (str): The page name (e.g., 'cto-as-a-service', 'ai-business-playbook', 'blog-ai-basics')
    """
    print(f"Generating specific page: {page_name}")
    
    # Define page mappings
    page_mappings = {
        'cto-as-a-service': {'route': '/cto-as-a-service.html', 'template': 'cto-as-a-service.html'},
        'ai-business-playbook': {'route': '/ai-business-playbook.html', 'template': 'ai-business-playbook.html'},
        'ai-for-video': {'route': '/ai-for-video.html', 'template': 'ai-for-video.html'},
        'ai-for-podcast': {'route': '/ai-for-podcast.html', 'template': 'ai-for-podcast.html'},
        'smart-business': {'route': '/smart-business.html', 'template': 'smart-business.html'},
        'bot-builder': {'route': '/bot-builder.html', 'template': 'bot-builder.html'},
        'ideas-to-stories': {'route': '/ideas-to-stories.html', 'template': 'ideas-to-stories.html'},
        'training-services': {'route': '/training-services.html', 'template': 'training-services.html'},
        'getting-started': {'route': '/getting-started.html', 'template': 'getting-started.html'},
        'business-services': {'route': '/business-services.html', 'template': 'business-services.html'},
        'contact': {'route': '/contact.html', 'template': 'contact.html'},
        'test-contact': {'route': '/test-contact.html', 'template': 'test-contact.html'},
        'index': {'route': '/', 'template': 'index.html'},
    }
    
    # Handle blog pages
    if page_name.startswith('blog-'):
        route_path = f'/blog/{page_name.replace("blog-", "")}.html'
        template_name = f'{page_name}.html'
    elif page_name in page_mappings:
        route_path = page_mappings[page_name]['route']
        template_name = page_mappings[page_name]['template']
    else:
        print(f"Error: Unknown page name '{page_name}'")
        print("Available pages:")
        for key in page_mappings.keys():
            print(f"  - {key}")
        print("For blog pages, use format: blog-{name}")
        return
    
    # Use the main app with proper configuration
    app.config['SERVER_NAME'] = 'localhost'
    app.config['APPLICATION_ROOT'] = '/'
    app.config['PREFERRED_URL_SCHEME'] = 'http'
    
    # Create application context and render the template
    with app.app_context():
        try:
            # Render the template
            rendered_content = render_template(template_name)
            
            # Determine output file path
            if route_path == '/':
                output_path = os.path.join('output', 'index.html')
            else:
                output_path = os.path.join('output', route_path.lstrip('/'))
            
            # Create directory if it doesn't exist
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            
            # Write the file
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(rendered_content)
            
            print(f"Page '{page_name}' generated successfully at {output_path}!")
            
        except Exception as e:
            print(f"Error generating page '{page_name}': {str(e)}")
            return

def show_available_commands():
    """Show available generation commands"""
    print("\n" + "="*60)
    print("AVAILABLE GENERATION COMMANDS")
    print("="*60)
    print("1. generate_homepage()           - Generate only the homepage")
    print("2. generate_all_blog_pages()     - Generate all blog pages")
    print("3. generate_specific_blog_page('blog-ai-basics') - Generate specific blog page")
    print("4. generate_main_pages()         - Generate all main pages (non-blog)")
    print("5. generate_specific_page('cto-as-a-service') - Generate specific page")
    print("6. generate_whole_website()      - Generate complete website + sitemap")
    print("7. generate_sitemap()            - Generate only sitemap.xml")
    print("8. show_available_commands()     - Show this help")
    print("\nExample usage:")
    print("  python -c \"from generate import generate_homepage; generate_homepage()\"")
    print("  python -c \"from generate import generate_specific_blog_page; generate_specific_blog_page('blog-ai-rag')\"")
    print("  python -c \"from generate import generate_specific_page; generate_specific_page('cto-as-a-service')\"")
    print("  python -c \"from generate import generate_whole_website; generate_whole_website()\"")
    print("\nOr in Python shell:")
    print("  python")
    print("  >>> from generate import *")
    print("  >>> generate_homepage()")
    print("  >>> generate_specific_blog_page('blog-ai-basics')")
    print("="*60)

if __name__ == '__main__':
    # Freeze the site
    freezer.freeze()
    
    # Generate sitemap after freezing
    # generate_sitemap()
    generate_homepage()
