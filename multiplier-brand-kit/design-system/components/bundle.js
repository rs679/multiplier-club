/* @ds-bundle: {"format":4,"namespace":"Multiplier","components":[{"name":"Logo"},{"name":"Button"},{"name":"Tag"},{"name":"Field"},{"name":"Card"},{"name":"Nav"},{"name":"DealCard"}]} */
(function () {
  var React = window.React;
  var h = React.createElement;

  function cx() {
    return Array.prototype.filter.call(arguments, Boolean).join(' ');
  }

  var MARK = 'M-13.47 -13.47A22 22 0 0 1 13.47 13.47A22 22 0 0 1 -13.47 -13.47ZM-13.47 13.47A22 22 0 0 1 13.47 -13.47A22 22 0 0 1 -13.47 13.47Z';

  function inkFor(tone) {
    if (tone === 'light') return 'var(--logo-white)';
    if (tone === 'dark') return 'var(--logo-black)';
    return 'var(--logo)';
  }

  function Logo(props) {
    var size = props.size || 32;
    var markOnly = !!props.markOnly;
    var ink = inkFor(props.tone);
    var mark = h(
      'svg',
      {
        className: 'mp-logo-mark',
        width: size,
        height: size,
        viewBox: '0 0 32 32',
        role: markOnly ? 'img' : undefined,
        'aria-label': markOnly ? 'Multiplier' : undefined,
        'aria-hidden': markOnly ? undefined : 'true'
      },
      h('path', { transform: 'translate(16 16)', fill: ink, fillRule: 'evenodd', d: MARK })
    );
    if (markOnly) return mark;
    return h(
      'span',
      { className: cx('mp-logo', props.className), style: { color: ink, gap: Math.round(size * 0.3) + 'px' } },
      mark,
      h('span', { className: 'mp-logo-word', style: { fontSize: Math.round(size * 1.08) + 'px' } }, 'multiplier')
    );
  }

  function Button(props) {
    var variant = props.variant || 'primary';
    var size = props.size || 'md';
    var cls = cx('mp-btn', 'mp-btn-' + variant, 'mp-btn-' + size, props.className);
    if (props.href) {
      return h('a', { className: cls, href: props.href, onClick: props.onClick }, props.children);
    }
    return h(
      'button',
      { className: cls, type: props.type || 'button', disabled: props.disabled, onClick: props.onClick },
      props.children
    );
  }

  function Tag(props) {
    var tone = props.tone || 'neutral';
    return h('span', { className: cx('mp-tag', 'mp-tag-' + tone, props.className) }, props.children);
  }

  function Field(props) {
    var id = React.useId();
    var describedBy = props.error ? id + '-msg' : props.hint ? id + '-msg' : undefined;
    var input = {
      id: id,
      className: cx('mp-input', props.error && 'mp-input-error'),
      type: props.type || 'text',
      placeholder: props.placeholder,
      disabled: props.disabled,
      onChange: props.onChange,
      'aria-invalid': props.error ? 'true' : undefined,
      'aria-describedby': describedBy
    };
    if (props.value !== undefined) input.value = props.value;
    else if (props.defaultValue !== undefined) input.defaultValue = props.defaultValue;
    return h(
      'div',
      { className: cx('mp-field', props.className) },
      h('label', { className: 'mp-label', htmlFor: id }, props.label),
      h('input', input),
      props.error
        ? h('span', { id: id + '-msg', className: 'mp-field-msg mp-field-err' }, props.error)
        : props.hint
        ? h('span', { id: id + '-msg', className: 'mp-field-msg' }, props.hint)
        : null
    );
  }

  function Card(props) {
    var tone = props.tone || 'raised';
    return h(
      'div',
      { className: cx('mp-card', 'mp-card-' + tone, props.className) },
      props.eyebrow ? h('span', { className: 'mp-eyebrow' }, props.eyebrow) : null,
      props.children
    );
  }

  function Nav(props) {
    var links = props.links || [];
    return h(
      'nav',
      { className: cx('mp-nav', props.className), 'aria-label': 'Primary' },
      h('a', { className: 'mp-nav-brand', href: props.homeHref || '#', 'aria-label': 'Multiplier home' }, h(Logo, { size: 28 })),
      h(
        'ul',
        { className: 'mp-nav-links' },
        links.map(function (l) {
          return h(
            'li',
            { key: l.label },
            h(
              'a',
              { href: l.href || '#', className: cx('mp-nav-link', l.current && 'is-current'), 'aria-current': l.current ? 'page' : undefined },
              l.label
            )
          );
        })
      ),
      h('div', { className: 'mp-nav-actions' }, props.actions)
    );
  }

  function DealCard(props) {
    return h(
      'article',
      { className: cx('mp-card', 'mp-card-raised', 'mp-deal', props.className) },
      h(
        'header',
        { className: 'mp-deal-head' },
        h('span', { className: 'mp-eyebrow' }, props.assetClass),
        props.status ? h(Tag, { tone: props.statusTone || 'accent' }, props.status) : null
      ),
      h('h3', { className: 'mp-deal-title' }, props.title),
      props.summary ? h('p', { className: 'mp-deal-summary' }, props.summary) : null,
      h(
        'dl',
        { className: 'mp-deal-rows' },
        h('div', null, h('dt', null, 'Minimum'), h('dd', null, props.minimum)),
        h('div', null, h('dt', null, 'Referral fee'), h('dd', null, props.fee))
      ),
      props.action ? h('div', { className: 'mp-deal-action' }, props.action) : null
    );
  }

  window.Multiplier = { Logo: Logo, Button: Button, Tag: Tag, Field: Field, Card: Card, Nav: Nav, DealCard: DealCard };
})();
