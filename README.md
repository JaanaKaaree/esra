# esra
Esra home page


# Run Generate scripts
.\venv\Scripts\Activate.ps1

# Generate Page Commands

### Generate only homepage
python -c "from generate import generate_homepage; generate_homepage()"

### Generate specific blog page
python -c "from generate import generate_specific_blog_page; generate_specific_blog_page('blog-ai-rag')"

### Generate all blog pages
python -c "from generate import generate_all_blog_pages; generate_all_blog_pages()"

### Generate main pages only
python -c "from generate import generate_main_pages; generate_main_pages()"

### Generate whole website
python -c "from generate import generate_whole_website; generate_whole_website()"

### Show help
python -c "from generate import show_available_commands; show_available_commands()"

### Specific page
python -c "from generate import generate_specific_page; generate_specific_page('cto-as-a-service')"


# Manual Deploy Changes 



# Git hub pipleline