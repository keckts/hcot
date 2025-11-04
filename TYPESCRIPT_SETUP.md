# TypeScript Setup for HCOT

This document explains the TypeScript setup in your Django project.

## Structure

```
hcot/
├── src/
│   └── ts/              # TypeScript source files
│       └── main.ts      # Sample TypeScript file
├── static/
│   └── js/              # Compiled JavaScript output
│       ├── main.js      # Compiled JavaScript
│       └── main.js.map  # Source map for debugging
├── tsconfig.json        # TypeScript configuration
└── package.json         # Node.js dependencies and scripts
```

## What Was Set Up

1. **TypeScript Installation**: TypeScript was added as a dev dependency via npm
2. **Directory Structure**:
   - `src/ts/` - Write your TypeScript files here
   - `static/js/` - Compiled JavaScript files go here (auto-generated)
3. **TypeScript Configuration**: `tsconfig.json` configured to:
   - Target ES6
   - Output to `static/js/`
   - Generate source maps for debugging
   - Enable strict type checking
4. **Sample File**: `src/ts/main.ts` with a simple "Hello from TypeScript!" example
5. **Base Template**: Added the compiled JavaScript to `base.html` so it loads on all pages

## Usage

### Compile TypeScript Once
```bash
npm run build
```

### Watch Mode (Auto-compile on changes)
```bash
npm run watch
```

### Adding New TypeScript Files

1. Create a new `.ts` file in `src/ts/`
2. Run `npm run build` to compile
3. The compiled `.js` file will appear in `static/js/`
4. Add it to your template with `{% static 'js/filename.js' %}`

## Testing

To verify TypeScript is working:

1. Start your Django server:
   ```bash
   source venv/bin/activate
   python manage.py runserver
   ```

2. Open your browser and visit http://localhost:8000

3. Open the browser console (F12 or right-click → Inspect → Console)

4. You should see:
   ```
   Hello from TypeScript!
   TypeScript is working!
   2 + 3 = 5
   ```

## Development Workflow

1. Edit TypeScript files in `src/ts/`
2. Run `npm run build` (or `npm run watch` for auto-compilation)
3. Refresh your browser to see changes
4. The compiled JavaScript is automatically served by Django's static files system

## Notes

- The `static/js/` directory contains compiled output - don't edit these files directly
- Always edit the `.ts` files in `src/ts/`
- Source maps are generated for easier debugging in the browser
- The compiled JavaScript is loaded as an ES6 module in base.html
