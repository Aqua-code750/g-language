Write-Host "Building VS Code Extension for G Language..."
cd vscode-extension
npx @vscode/vsce package --no-dependencies
Write-Host "Build complete! Look for the .vsix file in the vscode-extension folder."
