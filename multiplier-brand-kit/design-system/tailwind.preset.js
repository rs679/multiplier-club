// Tailwind preset for Multiplier. Import tokens.css once, then add this as a preset.
// Switch themes with data-theme="dark" (default) or data-theme="light" on <html>.
module.exports = {
  theme: {
    colors: {
      transparent: 'transparent',
      'bg': 'var(--bg)',
      'bg-raised': 'var(--bg-raised)',
      'bg-pine': 'var(--bg-pine)',
      'bg-navy': 'var(--bg-navy)',
      'border': 'var(--border)',
      'border-control': 'var(--border-control)',
      'ink': 'var(--ink)',
      'ink-muted': 'var(--ink-muted)',
      'ink-subtle': 'var(--ink-subtle)',
      'accent': 'var(--accent)',
      'teal': 'var(--teal)',
      'action': 'var(--action)',
      'action-hover': 'var(--action-hover)',
      'on-action': 'var(--on-action)',
      'focus': 'var(--focus)',
      'logo': 'var(--logo)',
      'logo-white': 'var(--logo-white)',
      'logo-black': 'var(--logo-black)',
      'positive': 'var(--positive)',
      'caution': 'var(--caution)',
      'critical': 'var(--critical)',
      'chart-teal': 'var(--chart-teal)',
      'chart-navy': 'var(--chart-navy)',
      'chart-slate': 'var(--chart-slate)'
    },
    spacing: {
      '0': '0',
      '1': 'var(--space-1)',
      '2': 'var(--space-2)',
      '3': 'var(--space-3)',
      '4': 'var(--space-4)',
      '5': 'var(--space-5)',
      '6': 'var(--space-6)',
      '7': 'var(--space-7)',
      '8': 'var(--space-8)',
      '9': 'var(--space-9)',
      '10': 'var(--space-10)'
    },
    borderRadius: {
      'none': 'var(--radius-none)',
      'sm': 'var(--radius-sm)',
      'md': 'var(--radius-md)',
      'icon': 'var(--radius-icon)'
    },
    fontFamily: {
      sans: ['Geist', 'Helvetica Neue', 'Arial', 'sans-serif'],
      mono: ['Geist Mono', 'ui-monospace', 'Menlo', 'Consolas', 'monospace'],
    },
    boxShadow: { none: 'none' },
  },
};
