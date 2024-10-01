'''
A System for Tabular data to Knowledge Graph Matching

main.py: Run this file and type in the number associated with the LLM you wish to execute

Created in 2024
@author: dylanlty
'''

import sys
import subprocess


def exec_llms():
    
    scripts = {
        '1': ('cea-gemini.py', 'gemini_console.log'),
        '2': ('cea-openai.py', 'openai_console.log'),
        '3': ('cea-hf.py', 'hf_console.log')
    }

    processes = []
    
    for i, (script, output_file) in scripts.items():
        with open(output_file, 'w') as f:
            # Start each script and redirect output to the corresponding file
            process = subprocess.Popen([sys.executable, script], stdout=f, stderr=subprocess.STDOUT)
            processes.append(process)
            print(f"Started {script}, output will be saved to {output_file}.")

    # Wait for all processes to complete
    for process in processes:
        process.wait()

    print("\nAll scripts completed.")

def main():

    print("\nSelect the LLM you want to run:")
    print(" [1] Gemini-1.5-flash")
    print(" [2] GPT-4o-mini")
    print(" [3] Meta-Llama-3-8B-Instruct")
    print(" [4] Run all models")

    inp = input("> ")
    print()

    if inp == '1':
        script = 'cea-gemini.py'
    elif inp == '2':
        script = 'cea-openai.py'
    elif inp == '3':
        script = 'cea-hf.py'
    elif inp == '4':
        exec_llms()
        return
    else:
        print("Invalid Script")
        return

    try:
        subprocess.run([sys.executable, script])
    except Exception as e:
        print(f"\nError running {script} - {e}")

if __name__ == "__main__":

    main()