Write-Host "Building g.exe..."
pyinstaller --onefile --name "g" --paths src --hidden-import modules.game --hidden-import modules.app --hidden-import modules.math --hidden-import modules.fs --hidden-import modules.os --hidden-import modules.automations --hidden-import modules.ai --hidden-import idle --hidden-import customtkinter --collect-all pkg_resources --collect-all jaraco --collect-all platformdirs src/g_cli.py

Write-Host "Building VS Code Extension..."
cd vscode-extension
npx @vscode/vsce package --no-dependencies
cd ..

Write-Host "Installing locally..."
code --install-extension vscode-extension/g-language-1.2.0.vsix --force

Write-Host "Committing to Git..."
git add .
git commit -m "v1.2.0 - Batteries Included Update (Math, FS, OS, AI, Automations)"
git push origin master

Write-Host "Publishing GitHub Release..."
gh release create v1.2.0 "dist/g.exe" "vscode-extension/g-language-1.2.0.vsix" -t "v1.2.0 - The Batteries Included Update" -n "Added standard library modules: math, fs, os, automations, and ai!"

Write-Host "Update Complete!"
