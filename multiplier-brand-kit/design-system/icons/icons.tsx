import type { ReactNode } from "react";

/** Multiplier icon set: 24 monoline icons on a 32 grid, one signature teal node each. */
const paths: Record<string, ReactNode> = {
  request: (<><circle cx='17' cy='16' r='10'/><path d='M3 16h11M10.5 12.5L14 16l-3.5 3.5'/><circle className='mi-a' cx='17' cy='16' r='2.4'/></>),
  verify: (<><circle cx='16' cy='16' r='11.5'/><path d='M10.5 16.5l3.8 3.8 7.2-8'/><circle className='mi-a' cx='24.2' cy='7.8' r='2.4'/></>),
  onboard: (<><circle className='mi-a' cx='7.5' cy='16' r='3.6'/><circle cx='25' cy='7' r='3'/><circle cx='25' cy='16' r='3'/><circle cx='25' cy='25' r='3'/><path d='M11 14.6L22 8M11.4 16H22M11 17.4L22 24'/></>),
  curate: (<><circle cx='5.5' cy='7' r='2.2'/><circle cx='5.5' cy='16' r='2.2'/><circle cx='5.5' cy='25' r='2.2'/><path d='M8 7.6L19 14.4M8 16h9M8 24.4l11-8.4'/><circle cx='23' cy='16' r='6'/><circle className='mi-a' cx='23' cy='16' r='2.4'/></>),
  review: (<><path d='M8.5 4.5h10.2l5.3 5.3V26a2.5 2.5 0 0 1-2.5 2.5H8.5A2.5 2.5 0 0 1 6 26V7a2.5 2.5 0 0 1 2.5-2.5z'/><path d='M18.5 4.8v5.4H24M10.5 15.5h9M10.5 19.5h6'/><circle className='mi-a' cx='20' cy='23.5' r='2.4'/></>),
  sign: (<><path d='M5 7.5A2.5 2.5 0 0 1 7.5 5h17A2.5 2.5 0 0 1 27 7.5v17a2.5 2.5 0 0 1-2.5 2.5h-17A2.5 2.5 0 0 1 5 24.5z'/><path d='M9.5 19.5c2.2-5.5 3.3-6 4-4.2.8 2 1.6 2.4 2.7-.2.7-1.7 1.6-1.4 2.3.3'/><path className='mi-ac' d='M9.5 23.2h13'/></>),
  fund: (<><circle cx='12.4' cy='16' r='8.4'/><circle cx='19.6' cy='16' r='8.4'/><circle className='mi-a' cx='16' cy='16' r='2.4'/></>),
  report: (<><circle cx='16' cy='16' r='10.5'/><circle cx='16' cy='16' r='4.2'/><path className='mi-ac' strokeWidth='3.4' d='M16 5.5a10.5 10.5 0 0 1 10.1 7.6'/></>),
  access: (<><circle cx='10.5' cy='16' r='6'/><circle className='mi-a' cx='10.5' cy='16' r='2.2'/><path d='M16.5 16H29M24.5 16v4M28.5 16v3'/></>),
  investor: (<><circle cx='16' cy='10.5' r='5'/><path d='M6 27.5a10 10 0 0 1 20 0'/><circle className='mi-a' cx='24.6' cy='7.6' r='2.3'/></>),
  sponsor: (<><rect x='4.5' y='13' width='9' height='14.5' rx='2'/><rect x='13.5' y='4.5' width='14' height='23' rx='2.5'/><path d='M17.5 10h6M17.5 14.5h6M17.5 19h3'/><circle className='mi-a' cx='9' cy='20.4' r='1.9'/></>),
  adviser: (<><circle cx='13' cy='9.5' r='4.6'/><path d='M4 25.5a9 9 0 0 1 14.4-7.2'/><circle cx='23.6' cy='22.6' r='5.2'/><path className='mi-ac' d='M21 22.8l1.9 1.9 3.5-4'/></>),
  secure: (<><rect x='6.5' y='14' width='19' height='13.5' rx='3'/><path d='M10.5 14v-3.2a5.5 5.5 0 0 1 11 0V14'/><circle className='mi-a' cx='16' cy='20.5' r='2.3'/></>),
  regulated: (<><path d='M16 3.8l9.5 3.7v7.3c0 6.2-4 10.2-9.5 13.2-5.5-3-9.5-7-9.5-13.2V7.5z'/><path d='M11.3 15.6l3.3 3.2 6.3-6.9'/></>),
  global: (<><circle cx='16' cy='16' r='11.5'/><ellipse cx='16' cy='16' rx='5' ry='11.5'/><path d='M4.8 16h22.4'/><circle className='mi-a' cx='25.2' cy='9.4' r='2.4'/></>),
  digital: (<><rect x='5' y='6' width='22' height='15' rx='2.8'/><path d='M12 26h8M16 21v5'/><circle className='mi-a' cx='16' cy='13.5' r='2.4'/></>),
  terms: (<><circle className='mi-a' cx='7.5' cy='9' r='2.1'/><path d='M13 9h14'/><circle cx='7.5' cy='16' r='2.1'/><path d='M13 16h14'/><circle cx='7.5' cy='23' r='2.1'/><path d='M13 23h9'/></>),
  reach: (<><circle cx='16' cy='16' r='11.5'/><circle cx='16' cy='16' r='6.2'/><circle className='mi-a' cx='16' cy='16' r='2.1'/><path d='M16 2.5v4.5M16 25v4.5M2.5 16H7M25 16h4.5'/></>),
  tailored: (<><path d='M5 10h22M5 22h22'/><circle cx='11' cy='10' r='3.2' fill='var(--bg-raised)'/><circle className='mi-a' cx='21' cy='22' r='3.2'/></>),
  team: (<><circle cx='11.6' cy='16' r='7.6'/><circle cx='20.4' cy='16' r='7.6'/><circle className='mi-a' cx='16' cy='9.4' r='2.2'/></>),
  mail: (<><rect x='4.5' y='7' width='23' height='18' rx='3'/><path d='M5.5 9.5L16 17.5l10.5-8'/><circle className='mi-a' cx='23.6' cy='21.2' r='2'/></>),
  insights: (<><path d='M16 8.5C13 6 9 5.5 5 6v17.5c4-.5 8 0 11 2.5 3-2.5 7-3 11-2.5V6c-4-.5-8 0-11 2.5zM16 8.5V26'/><circle className='mi-a' cx='22' cy='12.5' r='2.2'/></>),
  faq: (<><circle cx='16' cy='16' r='11.5'/><path d='M12.6 12.6a3.6 3.6 0 1 1 5.2 3.2c-1.1.6-1.8 1.4-1.8 2.7'/><circle className='mi-a' cx='16' cy='22.4' r='1.6'/></>),
  legal: (<><path d='M16 5v22M8.5 27h15M6 10.5h20'/><path d='M7 10.5l-3.6 7.6a4.2 2.7 0 0 0 7.2 0zM25 10.5l-3.6 7.6a4.2 2.7 0 0 0 7.2 0z'/><circle className='mi-a' cx='16' cy='5.2' r='2.2'/></>),
};
export type IconName = keyof typeof paths;
export const iconNames = Object.keys(paths) as IconName[];

export function MIcon({ name, size = 24, className = "", title }: { name: IconName; size?: number; className?: string; title?: string }) {
  return (
    <svg
      viewBox="0 0 32 32"
      width={size}
      height={size}
      className={`mi ${className}`}
      aria-hidden={title ? undefined : true}
      role={title ? "img" : undefined}
      aria-label={title}
      focusable="false"
    >
      {paths[name]}
    </svg>
  );
}
