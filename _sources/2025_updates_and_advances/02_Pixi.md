## Pixi

### What is Pixi?

Pixi is a modern replacement for conda. If you use conda environments, pixi does the same job but **faster** and **more reliable**. It creates reproducible environments from a single `pixi.toml` file, eliminating "works on my machine" problems that plague conda workflows.

### Creating Environments

**Important:** Run these commands in a folder containing `pixi.toml` (e.g., `pixi/appose_napari_ai/`, `pixi/microsam_cellpose3/`, or `pixi/stardist/`).

**Create environment only:**
```bash
pixi install
```

**Create environment AND run a task:**
```bash
pixi run startup
```

## Load environment in VSCode

To run a script with a pixi created environment

[ctrl][shift][p] to open command pallette   
'Python: Select Interpreter'  
'Enter Interpreter Path'  
'Browse your file system'  

Then (see below screenshot) select Python interpreter

![no image found](selectpython.png)

## Make Pixi Environment Available to VS Code Notebooks

### Register as Jupyter Kernel

This makes your environment appear in the kernel selector dropdown:

For example to make the ```appose_napari_ai``` environment available you would run the below command in the `pixi/appose_napari_ai/` folder.  For different environments you would change folder and environment display names. 

```bash
pixi run python -m ipykernel install --user --name=appose_napari_ai --display-name "Pixi (appose_napari_ai)"
```

**Note If this fails with "No module named ipykernel":**
1. First add ipykernel to your project: `pixi add ipykernel`
2. Then run the command above

### Troubleshooting

- **"No module ipykernel"**: Add it with `pixi add ipykernel` first
- **Can't find environment**: Use `pixi info` to see environment path
- **Kernel not showing up**: Restart VS Code after registering kernel

#### Using Pixi Shell for Proper Environment Setup

For environments that need special DLLs (like CUDNN), use `pixi shell` to ensure all paths are set correctly:

1. Navigate to your environment folder (e.g., `pixi/microsam_cellposesam/`)
2. Run `pixi shell` to activate the environment with all paths
3. Start VS Code from within the shell: `code .`

This ensures VS Code inherits the complete environment setup, including DLL paths that might be missing otherwise.