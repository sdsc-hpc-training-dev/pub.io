import yaml
import re

def load_yaml(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def extract_version(file_id):
    match = re.search(r':(\d+\.\d+\.\d+)', file_id)
    if match:
        return match.group(1)
    return "Unknown version"

def get_category_class(category):
    # Define the CSS class based on category
    category_classes = {
        'Category1': 'category1',
        'Category2': 'category2',
        'Category3': 'category3',
    }
    return category_classes.get(category, 'default-category')

def generate_card(component):
    version = extract_version(component.get('id', ''))
    category = component.get('category', 'Uncategorized')
    category_class = get_category_class(category)
    return f"""
<div class="card {category_class}">
    <h3>{component['name']}</h3>
    <p class="version">Version: {version}</p>
    <p class="italic">Category: {category}</p>
    <p>{component['description']}</p>
    <p><a href="{component['trainingTutorialsUrl']}">Training Tutorials</a></p>
</div>
"""

def generate_cards(yaml_data):
    cards = ""
    for component in yaml_data.get('components', []):
        if component.get('trainingTutorialsAvailable', False):
            cards += generate_card(component)
    return cards

def write_to_index(content, index_file_path):
    with open(index_file_path, 'w') as file:
        file.write(content)

def main():
    yaml_file_path = 'docs/master.yaml'
    index_file_path = 'docs/index.md'

    yaml_data = load_yaml(yaml_file_path)
    cards_content = generate_cards(yaml_data)
    
    full_content = f"""
# ICICLE Training Catalog

<button class="toggle-button" onclick="toggleView()">Toggle View</button>

<div id="cards-container" class="list-view">
{cards_content}
</div>

<script>
function toggleView() {{
  var container = document.getElementById('cards-container');
  if (container.classList.contains('list-view')) {{
    container.classList.remove('list-view');
    container.classList.add('grid-view');
  }} else {{
    container.classList.remove('grid-view');
    container.classList.add('list-view');
  }}
}}
</script>
"""
    
    write_to_index(full_content, index_file_path)

if __name__ == "__main__":
    main()
