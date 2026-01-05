import json

# Archivo donde se guardarán los datos
FILE_JSON = "plugins.json"

# Intentar cargar datos existentes o crear lista vacía
try:
    with open(FILE_JSON, 'r', encoding='utf-8') as f:
        plugins_list = json.load(f)
    print(f"\033[31m✓ {len(plugins_list)} tools registered in the file.\033[31m")
except FileNotFoundError:
    plugins_list = []
    print("✓ new file")

# Pedir datos al usuario
print("\n" + "="*40)
print("data record")
print("="*40)

while True:
    print(f"\n \033[34mtools #{len(plugins_list) + 1}")
    print("-" * 20)
    name = input("Plugin name (no spaces, use hyphens or underscores: ").strip()
    if not name:
        print("❗the Plugin name should not be empty")
        break

    author = input("\nPlugin author (name): ").strip()
    if not author:
        print("❗the Plugin author should not be empty")
        break
   
    description = input("\nPlugin description (clear and short description of the plugin): ").strip()
    if not description:
        print("❗the description should not be empty")
        break

    git_url = input("\nPlugin repository (github): ").strip()
    if not git_url:
        print("❗the Plugin repo should not be empty")
        break

        
    plugins_dict = {
        
        "name": name,
        "author": author,
        "description": description,
        "git_url": git_url,
      }
    
    
    plugins_list.append(plugins_dict)
    print(f"✅ {name.title()} tool add")
    break

# Guardar todos los datos
with open(FILE_JSON, 'w', encoding='utf-8') as f:
    json.dump(plugins_list, f, indent=4, ensure_ascii=False)
    print(f"\n!Your data was added correctly")
