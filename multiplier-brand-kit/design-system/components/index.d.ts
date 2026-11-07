import * as React from 'react';

export interface LogoProps {
  /** 'auto' follows the theme (white on dark, black on light). 'light' forces white, 'dark' forces black. Default 'auto'. */
  tone?: 'auto' | 'light' | 'dark';
  /** Height of the mark in px. The wordmark scales with it. Default 32. */
  size?: number;
  /** Render the mark alone, with the accessible name "Multiplier". */
  markOnly?: boolean;
  className?: string;
}
export declare function Logo(props: LogoProps): React.ReactElement;

export interface ButtonProps {
  /** Default 'primary'. */
  variant?: 'primary' | 'secondary' | 'ghost';
  /** 'md' is 48px high, 'lg' is 56px. Default 'md'. */
  size?: 'md' | 'lg';
  /** When set, renders an anchor instead of a button. */
  href?: string;
  type?: 'button' | 'submit' | 'reset';
  disabled?: boolean;
  onClick?: (e: React.MouseEvent) => void;
  children?: React.ReactNode;
  className?: string;
}
export declare function Button(props: ButtonProps): React.ReactElement;

export interface TagProps {
  /** Default 'neutral'. Always put a word in the tag; never rely on colour alone. */
  tone?: 'neutral' | 'accent' | 'caution' | 'critical';
  children?: React.ReactNode;
  className?: string;
}
export declare function Tag(props: TagProps): React.ReactElement;

export interface FieldProps {
  label: string;
  type?: string;
  placeholder?: string;
  value?: string;
  defaultValue?: string;
  hint?: string;
  /** An error message. Replaces the hint and marks the input invalid. */
  error?: string;
  disabled?: boolean;
  onChange?: (e: React.ChangeEvent<HTMLInputElement>) => void;
  className?: string;
}
export declare function Field(props: FieldProps): React.ReactElement;

export interface CardProps {
  /** Surface: 'raised' (bg-raised), 'pine' (bg-pine) or 'navy' (bg-navy). Default 'raised'. */
  tone?: 'raised' | 'pine' | 'navy';
  /** Optional mono eyebrow in the accent colour. */
  eyebrow?: string;
  children?: React.ReactNode;
  className?: string;
}
export declare function Card(props: CardProps): React.ReactElement;

export interface NavLink { label: string; href?: string; current?: boolean }
export interface NavProps {
  links?: NavLink[];
  /** Buttons or links shown at the right. */
  actions?: React.ReactNode;
  homeHref?: string;
  className?: string;
}
export declare function Nav(props: NavProps): React.ReactElement;

export interface DealCardProps {
  /** e.g. 'Private equity'. Shown as the mono eyebrow. */
  assetClass: string;
  title: string;
  summary?: string;
  /** The minimum investment exactly as it should read, e.g. '[amount]'. */
  minimum: string;
  /** The referral fee exactly as it should read, e.g. '[x]%'. */
  fee: string;
  /** A word such as 'Open' or 'Closing soon'. */
  status?: string;
  statusTone?: 'neutral' | 'accent' | 'caution' | 'critical';
  /** A Button or link shown under the figures. */
  action?: React.ReactNode;
  className?: string;
}
export declare function DealCard(props: DealCardProps): React.ReactElement;
