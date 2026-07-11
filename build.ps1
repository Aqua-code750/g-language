Write-Host "Installing requirements..."
pip install -r requirements.txt
pip install jaraco.text jaraco.functools jaraco.context platformdirs packaging setuptools

Write-Host "Building G language executable..."
pyinstaller --onefile --name "g" --paths src --hidden-import modules.game --hidden-import modules.app --hidden-import idle --hidden-import customtkinter --collect-all pkg_resources --collect-all jaraco --collect-all platformdirs src/g_cli.py

Write-Host "Build complete! Executable is in the dist/ folder."
