import os 
import sys

def analyze_directory(folder_path):
    results = {
        "folder":folder_path,
        "total_files": 0,
        "total_folders": 0,
        "total_size": 0,
        "files_by_type": {},
        "largest_files": []
    }
    
    if not os.path.exists(folder_path):
        print(F"Error: Folder '{folder_path}' doesn't exist!")
        return results
    
    if not os.path.isdir(folder_path):
        print(F"Error: '{folder_path}' is not a folder!")
        return results

    for current_folder_path, subfolders, files in os.walk(folder_path):
        results["total_folders"] += 1
        
        for file_name in files:
            full_file_path = os.path.join(current_folder_path, file_name)
            
            try:
                file_size = os.path.getsize(full_file_path)
                
                results["total_files"] += 1
                results["total_size"] += file_size
                
                name_parts = file_name.split(".")
                if len(name_parts)>1:
                    file_extension ="." + name_parts[-1].lower()
                else:
                    file_extension = "[no extension]"
                    
                if file_extension in results["file by type"]:
                    results["files_by_type"][file_extension] += 1
                else:
                    results["files_by_type"][file_extension] = 1
                
                results["largest_files"].append({
                    "name": file_name,
                    "path": full_file_path,
                    "size":file_size 
                })  
            except PermissionError:
                print(f"Skipping (no permission): {file_name}")    
            except OSError as e:
                print(f"Skipping (error):{file_name} - {e}")

    return results

def convert_bytes_to_readable(size_in_bytes):
    if size_in_bytes < 1024:
        return f"{size_in_bytes} bytes"
    
    size_in_kb = size_in_bytes /1024
    if size_in_kb < 1024:
        return f"{size_in_kb:.2f} KB"
    
    size_in_mb = size_in_kb / 1024
    if size_in_mb < 1024:
        return f"{size_in_mb:.2f} MB"
    
    size_in_gb = size_in_mb / 1024
    return f"{size_in_gb:.2f} GB"

def display_results(results):
    print("\n" +"=" * 50)
    print("DIRECTORY ANALYSIS RESULTS")
    print("="*50)
    
    print(f"\n Folder analyzed: {results["folder"]}")
    print(f" Total files found: {results['total_files']}")
    print(f" Total folders found: {results['total_folders']}")
    print(f" Total size: {convert_bytes_to_readable(results['total_size'])}")
    
    if results["files_by_type"]:
        print("\n Files by type:")
        print("_"*30)
        
        sorted_types = sorted(results["file_by_type"].item(),key = lambda x: x[1], reverse =True)
        
        for file_type, count in sorted_types:
            print(f"{file_type:20}->{count:4} files")
            
    if results["largest_files"]:
        print("\n 5 Largest Files:")
        print("-"*50)

        sorted_largest_files = sorted(results ["largest_files"], key=lambda x: x["size"], reverse = True)        
        
        for i, file_info in enumerate(sorted_largest_files[:5],1):
            readable_size = convert_bytes_to_readable(file_info["size"])
            print(f"{i:2}. {readable_size:12} -> {file_info['name']}")
            
    print("\n" + "=" * 50)
    print("Analysis complete!")
    print("=" * 50)
    

def simple_menu():
    print("\n"+ "="*50)
    print("DIRECTORY TREE ANALYZER")
    print("="*50)
    print("This tool analyzes a folder and provides statistics about its contents.")
    print("\n"+"-"*50)
    
    print("Enter the folder path you want to analyze:")
    print(" • Type '.' for current folder")
    print(" • Type '..' for parent folder")    
    print(" • Or type any folder path e.g '/Users/YourName/Documents'")
    print("\n Or type 'quit' to exit")
    print("-"*50)
    
    folder_path = input("\n Your choice: ").strip()
    
    if folder_path.lower() in ["quit","exit","q"]:
        print("Exiting the program. Goodbye!")
        sys.exit(0)
        
    return folder_path


def main():
    while True:
        folder_path = simple_menu()
        
        if folder_path == ".":
            folder_path = os.getcwd()
        elif folder_path == "..":
            folder_path = os.path.dirname(os.getcwd())
            
        results = analyze_directory(folder_path)
        
        if results["total_files"] > 0  or results["total_folders"] > 0:
            display_results(results)
        else:
            print(f"\n Folder '{folder_path}' is empty or contains no accessible file")
            
        print("\n"+ "-"*50)
        
        choice = input("Analyze another folder? (yes/no):").strip().lower()
        if choice not in [ "yes","y"]:
            print("Exiting the program. Goodbye!")     
            break
      
if __name__ == "__main__":   
    try:
        main()
    except KeyboardInterrupt:     
        print("\n\nProgram interrupted. Goodbye!")
    except Exception as e:
        print(f"Oops! Something went wrong.")
        print("Please ensure you enter a valid folder path.")