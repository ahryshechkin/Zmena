class ReportComposite:
    def render(self):
        self.body()

    def title(self, name, idx, **metrics):
        text = ", ".join(f"{key}={value}" for key, value in metrics.items())
        return f"{name} {idx}: {text}"
