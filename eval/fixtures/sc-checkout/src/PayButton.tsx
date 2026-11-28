import { useState } from "react";

export function PayButton({ orderId }: { orderId: string }) {
  const [pending, setPending] = useState(false);
  return (
    <button
      disabled={pending}
      onClick={async () => {
        setPending(true);
        await fetch(`/api/orders/${orderId}/pay`, { method: "POST" });
        setPending(false);
      }}
    >
      Pay
    </button>
  );
}
