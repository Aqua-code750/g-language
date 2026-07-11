Write-Host "Building g.exe..."
pyinstaller --onefile --name "g" --paths src --hidden-import modules.game --hidden-import modules.app --hidden-import idle --hidden-import customtkinter --collect-all pkg_resources --collect-all jaraco --collect-all platformdirs src/g_cli.py

Write-Host "Building VS Code Extension..."
cd vscode-extension
npx @vscode/vsce package --no-dependencies
cd ..

Write-Host "Installing locally..."
code --install-extension vscode-extension/g-language-1.1.0.vsix --force

Write-Host "Committing to Git..."
git add .
git commit -m "v1.1.0 - Advanced Features Update"
git push origin master

Write-Host "Publishing GitHub Release..."
gh release create v1.1.0 "dist/g.exe" "vscode-extension/g-language-1.1.0.vsix" -t "v1.1.0 - The Advanced Update" -n "Added Custom Functions, Lists, Dictionaries, File I/O, and Networking to the G Language!"

Write-Host "Update Complete!"
