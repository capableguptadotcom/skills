export type Order = { id: string; total: number };

export type OrdersState = {
  loading: boolean;
  orders?: Order[];
  error?: string;
};

export type OrdersEvent =
  | { type: "fetch" }
  | { type: "loaded"; orders: Order[] }
  | { type: "failed"; message: string };

export const initialState: OrdersState = { loading: false };

export function reduce(state: OrdersState, event: OrdersEvent): OrdersState {
  switch (event.type) {
    case "fetch":
      return { ...state, loading: true };
    case "loaded":
      return { ...state, loading: false, orders: event.orders };
    case "failed":
      return { ...state, loading: false, error: event.message };
  }
}

export function statusText(state: OrdersState): string {
  if (state.error) return `Couldn't load orders: ${state.error}`;
  if (state.loading) return "Loading orders…";
  if (state.orders && state.orders.length === 0) return "No orders yet";
  if (state.orders) return `${state.orders.length} orders`;
  return "";
}
