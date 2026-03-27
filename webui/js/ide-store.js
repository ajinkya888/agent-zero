import { createStore } from "/js/AlpineStore.js";
import { store as fileEditorStore } from "/components/modals/file-editor/file-editor-store.js";

const model = {
    async handleAction(action, data) {
        console.log("[ideStore] Handling action:", action, data);
        if (action === "open_file") {
            const path = data.path;
            const name = path.split('/').pop();
            // Try to open file in editor
            try {
                await fileEditorStore.openFile({ name, path });
            } catch (e) {
                console.error("[ideStore] Failed to open file:", e);
            }
        } else if (action === "close_file") {
            fileEditorStore.closeFileEditor();
        }
    }
}

export const store = createStore("ide", model);
