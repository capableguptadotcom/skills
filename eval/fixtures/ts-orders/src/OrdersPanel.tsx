import { statusText, type OrdersState } from "./orderState.ts";

export function OrdersPanel({ state }: { state: OrdersState }) {
  return (
    <section aria-busy={state.loading}>
      <p role="status">{statusText(state)}</p>
      <ul>
        {(state.orders ?? []).map((order) => (
          <li key={order.id}>
            {order.id}: ${order.total.toFixed(2)}
          </li>
        ))}
      </ul>
    </section>
  );
}
