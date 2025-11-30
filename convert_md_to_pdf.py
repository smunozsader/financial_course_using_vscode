"""
Batch convert all Markdown files to PDF for easy reading.

This script finds all .md files in the course and converts them to PDF
using VS Code's Markdown PDF extension.

Requirements:
- VS Code with Markdown PDF extension installed
- Run this from the course root directory
"""

import os
import subprocess
import time
from pathlib import Path

def find_markdown_files(root_dir='.'):
    """Find all markdown files in the course."""
    md_files = []
    
    # Patterns to include
    patterns = [
        'Module_*/Module_*.md',
        'Module_*/01_*.md',
        'Tutorials/Tutorial_*.md',
        'START_HERE.md',
        'README.md',
        'QUICK_START_GUIDE.md',
        'HOW_TO_GET_STARTED.md'
    ]
    
    root_path = Path(root_dir)
    
    for pattern in patterns:
        md_files.extend(root_path.glob(pattern))
    
    # Remove duplicates and sort
    md_files = sorted(set(md_files))
    
    return md_files

def convert_to_pdf_vscode(md_file):
    """
    Convert markdown to PDF using VS Code Markdown PDF extension.
    
    This opens the file in VS Code and triggers the PDF export command.
    """
    md_path = Path(md_file).absolute()
    
    print(f"Converting: {md_file}")
    
    try:
        # Open file in VS Code
        subprocess.run(['code', str(md_path)], check=True)
        
        # Wait a moment for file to open
        time.sleep(2)
        
        # Execute Markdown PDF export command
        # Note: This requires the markdown-pdf extension to be installed
        subprocess.run([
            'code',
            '--command',
            'markdown-pdf.pdf'
        ], check=True)
        
        # Wait for PDF generation
        time.sleep(3)
        
        print(f"  ✅ Converted: {md_file}")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"  ❌ Error converting {md_file}: {e}")
        return False
    except Exception as e:
        print(f"  ❌ Unexpected error with {md_file}: {e}")
        return False

def convert_to_pdf_pandoc(md_file):
    """
    Alternative: Convert markdown to PDF using pandoc.
    
    This is more reliable for batch processing but requires pandoc installation.
    Install: brew install pandoc
    """
    md_path = Path(md_file)
    pdf_path = md_path.with_suffix('.pdf')
    
    print(f"Converting: {md_file}")
    
    # Set up environment with LaTeX path
    env = os.environ.copy()
    env['PATH'] = '/Library/TeX/texbin:' + env.get('PATH', '')
    
    try:
        # Use XeLaTeX engine for better Unicode/emoji support
        result = subprocess.run([
            'pandoc',
            str(md_path),
            '-o', str(pdf_path),
            '--pdf-engine=xelatex',
            '-V', 'geometry:margin=1in',
            '-V', 'mainfont=Arial Unicode MS',
            '--toc',
            '--toc-depth=2'
        ], check=True, capture_output=True, text=True, env=env)
        
        print(f"  ✅ Created: {pdf_path}")
        return True
        
    except FileNotFoundError:
        print("  ❌ pandoc not installed. Install with: brew install pandoc")
        return False
    except subprocess.CalledProcessError as e:
        # If LaTeX fails, provide error details
        print(f"  ❌ Error: {e.stderr[:100] if e.stderr else 'Conversion failed'}")
        return False

def main():
    """Main conversion process."""
    print("="*80)
    print("MARKDOWN TO PDF BATCH CONVERTER")
    print("="*80)
    print("\nFinding all markdown files in the course...\n")
    
    # Find all markdown files
    md_files = find_markdown_files()
    
    print(f"Found {len(md_files)} markdown files:\n")
    for f in md_files:
        print(f"  - {f}")
    
    print("\n" + "="*80)
    print("CONVERSION METHOD")
    print("="*80)
    print("\nChoose conversion method:")
    print("1. Pandoc (recommended - batch processing)")
    print("2. VS Code Markdown PDF (requires manual intervention)")
    print("3. List files only (no conversion)")
    
    choice = input("\nEnter choice (1-3): ").strip()
    
    if choice == '3':
        print("\nFiles listed. No conversion performed.")
        return
    
    print("\n" + "="*80)
    print("STARTING CONVERSION")
    print("="*80)
    print()
    
    success_count = 0
    fail_count = 0
    
    for md_file in md_files:
        if choice == '1':
            result = convert_to_pdf_pandoc(md_file)
        else:
            result = convert_to_pdf_vscode(md_file)
        
        if result:
            success_count += 1
        else:
            fail_count += 1
        
        print()  # Blank line between files
    
    # Summary
    print("="*80)
    print("CONVERSION COMPLETE")
    print("="*80)
    print(f"\n✅ Successful: {success_count}")
    print(f"❌ Failed: {fail_count}")
    print(f"📊 Total: {len(md_files)}")
    
    if choice == '1':
        print("\n📁 PDF files created in the same directory as markdown files")
    
    print("\n💡 TIP: You can now share these PDFs with Mauricio!")
    print("   He can read them on any device without needing VS Code.\n")

if __name__ == "__main__":
    main()
