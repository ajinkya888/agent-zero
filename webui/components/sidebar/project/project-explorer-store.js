import { createStore } from "/js/AlpineStore.js";
import { fetchApi } from "/js/api.js";
import { store as fileEditorStore } from "/components/modals/file-editor/file-editor-store.js";
import { store as chatsStore } from "/components/sidebar/chats/chats-store.js";

const model = {
    files: [],
    loading: false,
    currentProject: null,
    currentPath: "/",

    async init() {
        this.refresh();
    },

    async refresh() {
        const ctx = chatsStore.getSelectedContext();
        if (!ctx || !ctx.project) {
            this.files = [];
            this.currentProject = null;
            return;
        }

        if (this.currentProject !== ctx.project.name) {
            this.currentProject = ctx.project.name;
            this.currentPath = "/";
        }

        this.loading = true;
        try {
            const resp = await fetchApi(`/get_work_dir_files?path=${encodeURIComponent(this.currentPath)}`);
            const data = await resp.json();
            if (data.ok) {
                this.files = data.data || [];
            }
        } catch (e) {
            console.error("[projectExplorer] Refresh failed:", e);
        } finally {
            this.loading = false;
        }
    },

    async openFile(file) {
        if (file.type === "dir") {
            this.currentPath = file.path;
            await this.refresh();
        } else {
            await fileEditorStore.openFile(file, () => this.refresh());
        }
    },

    async goUp() {
        if (this.currentPath === "/") return;
        const parts = this.currentPath.split("/").filter(Boolean);
        parts.pop();
        this.currentPath = "/" + parts.join("/");
        await this.refresh();
    }
}

export const store = createStore("projectExplorer", model);
