/**
 * TTS via backend — chama /api/v1/tv/tts/?text=...
 * O backend usa Google Cloud TTS Wavenet pt-BR.
 * Se o backend retornar 503 (não configurado), usa Web Speech API como fallback.
 */

let currentAudio: HTMLAudioElement | null = null;

/** Verifica se o backend TTS está configurado via env var — sem fazer requests */
function isBackendTTSConfigured(): boolean {
  const key = process.env.NEXT_PUBLIC_GOOGLE_TTS_KEY ?? '';
  return key.length > 0 && key !== 'sua_chave_aqui';
}

function speakFallback(text: string, onStart?: () => void, onEnd?: () => void) {
  if (typeof window !== 'undefined' && window.speechSynthesis) {
    const utter = new SpeechSynthesisUtterance(text);
    utter.lang = 'pt-BR';
    utter.rate = 0.9;
    onStart?.();
    utter.onend = () => onEnd?.();
    window.speechSynthesis.speak(utter);
  }
}

export async function speakGoogleTTS(
  text: string,
  onStart?: () => void,
  onEnd?: () => void
): Promise<void> {
  if (currentAudio) {
    currentAudio.pause();
    currentAudio = null;
  }

  const available = isBackendTTSConfigured();
  if (!available) {
    speakFallback(text, onStart, onEnd);
    return;
  }

  try {
    const url = `/api/v1/tv/tts/?text=${encodeURIComponent(text)}`;
    const res = await fetch(url);

    if (res.status === 503) {
      speakFallback(text, onStart, onEnd);
      return;
    }

    if (!res.ok) throw new Error(`TTS error ${res.status}`);

    const blob = await res.blob();
    const audioUrl = URL.createObjectURL(blob);
    const audio = new Audio(audioUrl);
    currentAudio = audio;

    onStart?.();
    await audio.play();
    audio.onended = () => {
      URL.revokeObjectURL(audioUrl);
      currentAudio = null;
      onEnd?.();
    };
  } catch (err) {
    console.error('Google TTS falhou, usando fallback:', err);
    speakFallback(text, onStart, onEnd);
  }
}
