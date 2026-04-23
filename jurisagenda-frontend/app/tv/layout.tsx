export default function TVLayout({ children }: { children: React.ReactNode }) {
  // Força tema claro no painel TV — não deve herdar o dark mode do sistema
  return (
    <div className="light" style={{ colorScheme: 'light' }}>
      {children}
    </div>
  );
}
