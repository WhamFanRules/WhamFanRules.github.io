async function loadRules()
{
    const manifestResponse = await fetch("./manifest.json");
    const manifest = await manifestResponse.json();

    const container = document.getElementById("RulesSections");

    for (const [folder, files] of Object.entries(manifest))
    {
        const section = document.createElement("section");

        const heading = document.createElement("h2");
        heading.textContent = folder;
        section.appendChild(heading);

        for (const file of files)
        {
            const path = `${folder}/${file}`;

            const response = await fetch(path);
            const text = await response.text();

            const card = document.createElement("div");
            card.className = "rule-card";

            const title = file
                .replace(".txt", "")
                .replaceAll("_", " ");

            card.innerHTML = `
                <h3>${title}</h3>
                <a href="${path}" download>
                    <button>Download</button>
                </a>
                <pre>${text}</pre>
            `;

            section.appendChild(card);
        }

        container.appendChild(section);
    }
}

document.addEventListener("DOMContentLoaded", loadRules);