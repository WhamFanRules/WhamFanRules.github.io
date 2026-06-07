const express = require('express');
const fs = require('fs');
const path = require('path');

const app = express();
const port = 3000;

// Serve static files from the root directory
app.use(express.static(path.join(__dirname)));

// Serve static files from the Styles directory
app.use('/Styles', express.static(path.join(__dirname, 'Styles')));

// Serve static files from the Styles directory
app.use('/Scripts', express.static(path.join(__dirname, 'Scripts')));

app.use(express.static(path.join(__dirname, 'Factions/Necrons')));

app.get('/api/files', (req, res) => {
    const baseDir = path.join(__dirname, 'Factions/Necrons');
    fs.readdir(baseDir, { withFileTypes: true }, (err, files) => {
        if (err) {
            return res.status(500).json({ error: 'Failed to read directory' });
        }

        const data = {};
        files.forEach(file => {
            if (file.isDirectory()) {
                const folderPath = path.join(baseDir, file.name);
                const txtFiles = fs.readdirSync(folderPath).filter(f => f.endsWith('.txt'));
                data[file.name] = txtFiles;
            }
        });

        res.json(data);
    });
});

app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});