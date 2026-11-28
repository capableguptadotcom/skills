export type OrderStatus = "pending" | "paid" | "canceled";

export type Order = {
  id: string;
  status: OrderStatus;
  placedAt: Date;
  totalCents: number;
};

export function statusLabel(status: OrderStatus): string {
  switch (status) {
    case "pending":
      return "Awaiting payment";
    case "paid":
      return "Paid";
    case "canceled":
      return "Canceled";
    default: {
      const unknown: never = status;
      throw new Error(`unknown status ${unknown}`);
    }
  }
}
